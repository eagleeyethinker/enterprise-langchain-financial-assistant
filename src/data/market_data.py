import yfinance as yf

def get_stock_data(ticker: str):
    symbol = ticker.strip().upper()
    if not symbol:
        raise ValueError("Ticker cannot be empty.")

    try:
        stock = yf.Ticker(symbol)
        df = stock.history(period="1y")
    except Exception as exc:
        raise RuntimeError(
            f"Failed to fetch market data for '{symbol}'. Try again in a moment."
        ) from exc

    if df is None or df.empty:
        raise ValueError(f"No market data found for ticker '{symbol}'.")

    if "Close" not in df.columns:
        raise ValueError(f"Market data for '{symbol}' is missing Close prices.")

    return df
