
import ta

def compute_indicators(df):

    df["SMA50"] = df["Close"].rolling(window=50).mean()
    df["SMA200"] = df["Close"].rolling(window=200).mean()

    rsi = ta.momentum.RSIIndicator(df["Close"])
    df["RSI"] = rsi.rsi()

    latest = df.iloc[-1]

    return {
        "price": float(latest["Close"]),
        "SMA50": float(latest["SMA50"]),
        "SMA200": float(latest["SMA200"]),
        "RSI": float(latest["RSI"])
    }
