import matplotlib.pyplot as plt
import pandas as pd


def plot_raw_series(df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(3, 1, figsize=(14, 12), sharex=True)

    axes[0].plot(df.index, df["interest_rate"])
    axes[0].set_title("US 10Y Treasury Rate")

    axes[1].plot(df.index, df["usd_krw"])
    axes[1].set_title("USD/KRW Exchange Rate")

    axes[2].plot(df.index, df["sp500"])
    axes[2].set_title("S&P 500")

    plt.tight_layout()
    plt.show()


def plot_normalized(df: pd.DataFrame, title: str = "Normalized Comparison") -> None:
    plt.figure(figsize=(14, 6))
    for col in df.columns:
        plt.plot(df.index, df[col], label=col)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_correlation_matrix(corr: pd.DataFrame, title: str = "Correlation Matrix") -> None:
    plt.figure(figsize=(6, 5))
    plt.imshow(corr, interpolation="nearest", cmap="coolwarm", vmin=-1, vmax=1)
    plt.colorbar()
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.title(title)
    plt.tight_layout()
    plt.show()