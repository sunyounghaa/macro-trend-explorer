# Macro Trend Explorer

A beginner-friendly financial data analysis project that explores the relationships between U.S. interest rates, USD/KRW exchange rates, and the S&P 500 index.

---

## Motivation

Financial news is full of phrases like *"stocks fell on rate hike fears"* or *"won weakens as dollar strengthens."*

This project was built to move beyond intuition — to actually verify these relationships using real data, and to build a foundation for reading markets more analytically.

---

## What This Project Analyzes

- Trend visualization of interest rates, exchange rates, and equity index
- Normalized comparison of all three series on a single chart
- Monthly return and rate-of-change calculations
- Correlation analysis between rate changes, FX returns, and stock returns
- Daily vs. monthly data comparison

---

## Key Findings (2018–2026)

| Pair | Correlation |
|---|---|
| Rate change vs S&P 500 | -0.210 |
| FX return vs S&P 500 | -0.439 |
| Rate change vs FX return | +0.358 |

- When interest rates rise, stock returns tend to decline (weak negative)
- When the dollar strengthens (KRW weakens), stock returns tend to decline (moderate negative)
- When interest rates rise, the dollar tends to strengthen (moderate positive)

> Note: Correlation does not imply causation. Results vary by time period and data frequency.

---

## Data Sources

| Data | Source | Ticker |
|---|---|---|
| U.S. 10Y Treasury Rate | Yahoo Finance | `^TNX` |
| USD/KRW Exchange Rate | Yahoo Finance | `KRW=X` |
| S&P 500 Index | Yahoo Finance | `^GSPC` |

---

## Project Structure
```text
macro-trend-explorer/
├── README.md
├── requirements.txt
├── notebooks/
│   └── macro_analysis_starter.ipynb
├── src/
│   ├── data_loader.py
│   ├── analysis.py
│   └── plots.py
├── data/
│   ├── raw/
│   └── processed/
└── outputs/
    └── figures/
```

---

## How to Run
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Launch Jupyter
jupyter notebook

# 3. Open and run
notebooks/macro_analysis_starter.ipynb
```

---

## Skills Practiced

- Time series data processing with `pandas`
- Financial data retrieval with `yfinance`
- Data normalization and return calculation
- Correlation analysis and heatmap visualization
- Modular code structure (`src/` layout)

---

## Limitations

- This is not a predictive model
- Correlation results change significantly depending on the time period
- Causality cannot be inferred from correlation alone

---

## Future Improvements

- [ ] Add KOSPI index
- [ ] Add Korean interest rate data (Bank of Korea)
- [ ] Rolling correlation analysis
- [ ] Lag analysis (time-delayed correlation)
- [ ] Recession period comparison

---

*Built as a portfolio project for learning Python, time series analysis, and macro finance.*