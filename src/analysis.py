import pandas as pd


def make_monthly_analysis(df: pd.DataFrame) -> pd.DataFrame:
    monthly = df.resample("ME").last()
    monthly["fx_return"] = monthly["usd_krw"].pct_change()
    monthly["sp500_return"] = monthly["sp500"].pct_change()
    monthly["rate_change"] = monthly["interest_rate"].diff()
    return monthly.dropna()


def normalize_df(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    return df[columns] / df[columns].iloc[0] * 100


def correlation_table(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    return df[columns].corr()


def interpret_correlation(corr: pd.DataFrame) -> None:
    rate_stock = corr.loc["rate_change", "sp500_return"].item()
    fx_stock = corr.loc["fx_return", "sp500_return"].item()

    print("=== 해석 ===")
    if rate_stock < 0:
        print(f"금리 변화 vs S&P 500: {rate_stock:.3f} → 음의 관계")
    else:
        print(f"금리 변화 vs S&P 500: {rate_stock:.3f} → 양의 관계 또는 불분명")

    if fx_stock < 0:
        print(f"환율 변화 vs S&P 500: {fx_stock:.3f} → 반대 방향")
    else:
        print(f"환율 변화 vs S&P 500: {fx_stock:.3f} → 같은 방향 또는 불분명")