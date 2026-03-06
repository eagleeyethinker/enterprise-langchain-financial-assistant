
import os

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from prompts.analyst_prompt import analyst_prompt
from tools.stock_price_tool import stock_analysis

load_dotenv()

_llm = None


def _get_llm():
    global _llm
    if _llm is None:
        if not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError(
                "OPENAI_API_KEY is not set. Set it in your shell before calling /analyze/{ticker}."
            )
        _llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.2,
        )
    return _llm

def run_research(ticker):

    indicators = stock_analysis.invoke(ticker)

    prompt = analyst_prompt.format(**indicators)

    response = _get_llm().invoke(prompt)

    return response.content
