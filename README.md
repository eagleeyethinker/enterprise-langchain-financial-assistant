
# Enterprise LangChain Financial Research Assistant

Production-style LangChain project demonstrating a **financial research assistant**
that analyzes US stock market data using:

- LangChain
- yfinance market data
- technical indicators (SMA / RSI)
- LLM reasoning
- FastAPI API layer
- C4 architecture diagrams

Author: Satish Gopinathan – The Pragmatic Architect

---

## Features

- Real US stock market data retrieval
- Technical indicator calculation
- LLM financial analysis
- Agent-based tool orchestration
- Health endpoint for Yahoo Finance + OpenAI connectivity checks
- Graceful API error handling with clear HTTP status codes
- Enterprise repo structure
- C4 architecture documentation

---

## Quick Start

### 1) Create & activate a virtual environment (recommended)

**PowerShell (Windows)**

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Bash / WSL / macOS**

```
python -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```
pip install -r requirements.txt
```

### 3) Set your OpenAI API key (required for `/analyze/{ticker}`)

Recommended: create a `.env` file in the repo root:

```env
OPENAI_API_KEY=sk-your-real-key-here
```

**PowerShell**

```
$env:OPENAI_API_KEY = "<your-key-here>"
```

**Bash / WSL / macOS**

```
export OPENAI_API_KEY="<your-key-here>"
```

### 4) Run API

```
uvicorn api.main:app --reload --app-dir src
```

Alternative (without `--app-dir`):

```
uvicorn src.api.main:app --reload
```

### 5) Open API docs

```
http://127.0.0.1:8000/docs
```

## API Endpoints

### Analyze a ticker

```
GET /analyze/{ticker}
```

Example:

```
http://127.0.0.1:8000/analyze/AAPL
```

### Health check

```
GET /health
```

Example:

```
http://127.0.0.1:8000/health
```

Response shape:

```json
{
  "status": "ok | degraded",
  "timestamp_utc": "ISO-8601 timestamp",
  "checks": {
    "yahoo": {
      "ok": true,
      "error": "optional error message"
    },
    "openai": {
      "ok": true,
      "error": "optional error message"
    }
  }
}
```

Expected for a healthy setup:

- `checks.yahoo.ok` = `true`
- `checks.openai.ok` = `true`

## Error Handling

- `/analyze/{ticker}` returns `400` for invalid ticker/data errors.
- `/analyze/{ticker}` returns `503` for upstream dependency/config issues.
- If `OPENAI_API_KEY` is missing, analysis calls return a clear `503` message.
