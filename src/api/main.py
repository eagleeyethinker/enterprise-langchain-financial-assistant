
import os
from datetime import datetime, timezone

import yfinance as yf
from fastapi import FastAPI, HTTPException
from openai import OpenAI

try:
    # Works when running from repo root, e.g. `uvicorn src.api.main:app`
    from src.workflows.research_chain import run_research
except ModuleNotFoundError:
    # Works when using `--app-dir src`, e.g. `uvicorn api.main:app --app-dir src`
    from workflows.research_chain import run_research

app = FastAPI()

@app.get("/analyze/{ticker}")
def analyze(ticker: str):
    try:
        result = run_research(ticker)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Unexpected error while analyzing ticker.",
        ) from exc

    return {
        "ticker": ticker,
        "analysis": result
    }


@app.get("/health")
def health():
    checks = {
        "yahoo": {"ok": False},
        "openai": {"ok": False},
    }

    # Yahoo Finance connectivity and data availability check.
    try:
        df = yf.Ticker("MSFT").history(period="5d")
        if df is None or df.empty:
            checks["yahoo"]["error"] = "No data returned for test ticker."
        else:
            checks["yahoo"]["ok"] = True
    except Exception as exc:
        checks["yahoo"]["error"] = str(exc)

    # OpenAI API key + connectivity/auth check.
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        checks["openai"]["error"] = "OPENAI_API_KEY is not set."
    else:
        try:
            client = OpenAI(api_key=api_key)
            client.models.list()
            checks["openai"]["ok"] = True
        except Exception as exc:
            checks["openai"]["error"] = str(exc)

    overall_ok = checks["yahoo"]["ok"] and checks["openai"]["ok"]
    return {
        "status": "ok" if overall_ok else "degraded",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "checks": checks,
    }
