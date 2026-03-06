
from langchain.tools import tool
from data.market_data import get_stock_data
from tools.technical_analysis_tool import compute_indicators

@tool
def stock_analysis(ticker: str):
    """Fetch stock price history for a ticker and compute technical indicators."""

    df = get_stock_data(ticker)

    indicators = compute_indicators(df)

    return indicators
