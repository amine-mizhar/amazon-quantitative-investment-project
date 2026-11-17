# Amazon Quantitative Investment Project

## Overview

This project investigates whether machine-learning models can be used to generate an investment strategy for **Amazon (AMZN)** and whether such a strategy can provide attractive risk-adjusted performance compared with a traditional **Buy & Hold** approach.

The project combines financial data analysis, statistical analysis, machine learning, robustness testing, historical backtesting, and investment-performance evaluation.

The objective is not only to evaluate predictive accuracy, but also to determine whether predictive signals can translate into meaningful investment performance.

---

## Research Question

> **Can a machine-learning-based trading strategy generate competitive risk-adjusted returns compared with a passive Buy & Hold strategy for Amazon stock?**

---

## Project Objectives

The project aims to:

- Collect and prepare historical financial data.
- Perform statistical and exploratory analysis.
- Develop machine-learning models for market prediction.
- Evaluate model predictive performance.
- Convert model predictions into an investment strategy.
- Backtest the strategy using historical data.
- Compare the strategy with a Buy & Hold benchmark.
- Evaluate return, volatility, drawdown, and risk-adjusted performance.
- Test the robustness of the results.
- Assess the practical investment relevance of the strategy.

---

## Methodology

The analysis follows a complete quantitative-investment workflow:

### 1. Financial Data Collection

Historical market data for Amazon was collected and prepared for analysis.

The project also includes market data used for comparison and additional analysis.

### 2. Data Preparation

The raw financial data was cleaned and transformed into analysis-ready datasets.

Processed datasets are stored in:

```text
data/processed/
```

### 3. Statistical Analysis

The project includes statistical and exploratory analysis of market returns and related financial characteristics.

This stage provides the foundation for the subsequent machine-learning and investment analysis.

### 4. Machine Learning

Two classification models were evaluated:

- **Logistic Regression**
- **Random Forest**

The models were evaluated using predictive metrics including:

- Accuracy
- ROC-AUC

### 5. Investment Strategy

Model predictions were converted into investment signals.

The resulting signals were used to construct a historical machine-learning investment strategy.

The strategy was then compared with a passive Buy & Hold benchmark.

### 6. Robustness Analysis

The project includes robustness analysis and time-series cross-validation to reduce the risk of drawing conclusions from a single model evaluation.

### 7. Backtesting

The investment strategy was backtested using historical data.

The backtest tracks both:

- Strategy returns
- Buy & Hold returns

and their cumulative performance over the testing period.

---

## Key Results

The final backtest produced the following performance results:

| Metric | ML Strategy | Buy & Hold |
|---|---:|---:|
| Total Return | 11.32% | 28.72% |
| Annualized Volatility | 20.86% | 32.85% |
| Maximum Drawdown | -19.24% | -30.88% |
| Sharpe Ratio | 0.43 | 0.65 |

The machine-learning strategy generated a **positive return**, but it did not outperform the Buy & Hold benchmark in total return.

However, the strategy exhibited:

- Lower annualized volatility
- Smaller maximum drawdown

This indicates a trade-off between **return and risk**.

The results therefore do not provide sufficient evidence that the tested machine-learning strategy should replace a passive Buy & Hold approach for Amazon over the tested period.

---

## Machine-Learning Performance

The final model-performance evaluation included:

| Model | Accuracy | ROC-AUC | Total Return |
|---|---:|---:|---:|
| Logistic Regression | 49.75% | 0.5501 | 11.32% |
| Random Forest | 48.74% | 0.4923 | — |
| Buy & Hold | 53.27% | — | 28.72% |

The results show that predictive performance and investment performance are not necessarily equivalent.

In particular, a model can generate signals with some predictive value without necessarily producing a strategy that outperforms a passive investment benchmark.

---

## Risk-Adjusted Performance

The project also evaluates risk-adjusted performance using:

- Sharpe Ratio
- Sortino Ratio
- Annualized Volatility
- Maximum Drawdown

The main reliable comparison used in the final analysis shows that the ML strategy achieved lower volatility and a smaller maximum drawdown than Buy & Hold, while Buy & Hold achieved higher overall returns and a higher Sharpe Ratio.

---

## Main Conclusion

The results suggest that the tested machine-learning approach may provide some benefits in terms of risk management, but its predictive capability did not translate into superior investment performance over the tested period.

The project therefore does **not** support replacing a passive Buy & Hold strategy with the tested machine-learning strategy.

However, the machine-learning approach could potentially be useful as:

- An experimental signal-generation tool
- A supplementary risk-management tool
- A component of a broader quantitative investment framework

The conclusions should be interpreted cautiously because the analysis is based on historical market data. Relationships observed in historical data may not remain stable in future market conditions.

---

## Tools & Technologies

- **Python** — data analysis, statistical analysis, machine learning and backtesting
- **Jupyter Notebook** — research workflow and experimentation
- **Pandas / NumPy** — data processing and numerical analysis
- **Scikit-learn** — machine-learning models and evaluation
- **Power BI** — interactive analysis and visualization
- **Microsoft Excel** — investment-performance dashboard
- **SQL** — data/query component
- **Git / GitHub** — project version control and portfolio presentation

---

## Project Structure

```text
Amazon Quant Project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── excel/
│   └── amazon_quantitative_dashboard.xlsx
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_statistical_analysis.ipynb
│   └── 03_machine_learning.ipynb
│
├── powerbi/
│
├── report/
│   └── amazon_quantitative_research_report.md
│
├── sql/
│
├── src/
│
└── README.md
```

---

## Deliverables

### Research Notebooks

The `notebooks/` directory contains the main research workflow:

1. Data collection
2. Statistical analysis
3. Machine learning and investment backtesting

### Research Report

A complete research report is available in:

```text
report/amazon_quantitative_research_report.md
```

The report presents the methodology, results, investment relevance, limitations, and final conclusions.

### Excel Dashboard

The project includes an Excel investment dashboard containing the main performance indicators and comparison between the ML strategy and Buy & Hold.

### Power BI

Power BI was used during the analysis to visualize and compare strategy performance and investment returns.

---

## Limitations

Several limitations should be considered:

- The analysis is based on historical market data.
- Historical relationships may not remain stable in the future.
- Transaction costs and trading frictions can affect real-world performance.
- The tested machine-learning models represent a limited selection of possible approaches.
- Further research could test additional features, alternative algorithms, different time periods, and more sophisticated portfolio-management techniques.

---

## Future Improvements

Potential extensions include:

- Testing additional machine-learning algorithms.
- Engineering additional financial and market features.
- Testing different time periods.
- Incorporating transaction costs and trading frictions.
- Improving portfolio-management and position-sizing techniques.
- Testing the strategy on additional stocks or diversified portfolios.
- Performing more extensive out-of-sample testing.

---

## Final Takeaway

This project demonstrates a complete quantitative-investment research workflow, from financial data collection and statistical analysis to machine learning, time-series validation, backtesting, risk analysis, and investment-performance evaluation.

While the tested machine-learning strategy did not outperform Buy & Hold, the project demonstrates how machine-learning predictions can be evaluated not only from a predictive perspective, but also from a practical investment perspective.