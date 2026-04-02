import pandas as pd
import yfinance as yf


def load_macro_data(start_date: str, end_date: str) -> pd.DataFrame:
    """
    Load interest rate, USD/KRW exchange rate, and S&P 500 data.
    """
    rate = yf.download("^TNX", start=start_date, end=end_date, auto_adjust=False)
    rate = rate[["Close"]].rename(columns={"Close": "interest_rate"})

    fx = yf.download("KRW=X", start=start_date, end=end_date, auto_adjust=False)
    fx = fx[["Close"]].rename(columns={"Close": "usd_krw"})

    sp500 = yf.download("^GSPC", start=start_date, end=end_date, auto_adjust=False)
    sp500 = sp500[["Close"]].rename(columns={"Close": "sp500"})

    df = pd.concat([rate, fx, sp500], axis=1)
    df.columns = ["interest_rate", "usd_krw", "sp500"]
    df = df.sort_index().ffill().dropna()

    return df