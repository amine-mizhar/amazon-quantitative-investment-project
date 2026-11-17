# Amazon Quantitative Investment Strategy: Machine Learning and Backtesting

**Project:** Amazon Quant Project  
**Asset:** Amazon (AMZN)  
**Approach:** Statistical Analysis, Machine Learning, Backtesting and Risk Evaluation  
**Tools:** Python, SQL, Excel and Power BI

---

## 1. Executive Summary

This project investigates whether machine-learning techniques can be used to develop an investment strategy for Amazon (AMZN) stock.

The project follows a complete quantitative-investment workflow, beginning with financial data collection and preparation, followed by statistical analysis, machine-learning modelling, model evaluation, robustness testing, and historical backtesting. The resulting strategy is then compared with a simple Buy & Hold benchmark to evaluate its practical investment relevance.

Two machine-learning classification approaches were investigated: Logistic Regression and Random Forest. Their predictive performance was evaluated using classification metrics and ROC-AUC, while time-series cross-validation was used to assess the robustness of the results.

The machine-learning signals were subsequently converted into an investment strategy and evaluated through historical backtesting. The analysis considered return, annualized return, volatility, maximum drawdown, and other performance measures.

The backtest indicates that the machine-learning strategy generated a positive return during the tested period but did not outperform the Buy & Hold benchmark in terms of total and annualized return. However, the strategy exhibited lower volatility and a smaller maximum drawdown, suggesting a potential trade-off between return and risk.

Overall, the results do not provide sufficient evidence that the machine-learning strategy is superior to a passive Buy & Hold approach. Nevertheless, the project demonstrates how machine-learning models can be incorporated into a quantitative investment workflow and evaluated not only according to predictive accuracy, but also according to their practical investment performance and risk characteristics.

---

## 2. Project Objective

The objective of this project is to design and evaluate a simple machine-learning-based investment strategy for Amazon stock.

The project aims to determine whether historical market information can be used to generate predictive signals that translate into a potentially useful trading strategy. Rather than focusing exclusively on prediction accuracy, the project evaluates the strategy from an investment perspective by considering returns, risk, robustness, and performance relative to a passive benchmark.

The project also aims to demonstrate a complete quantitative-finance workflow using Python, SQL, Excel, and Power BI, from raw financial data through to analytical results and professional visualization.

---

## 3. Research Question

**Can a machine-learning model generate an investment strategy for Amazon stock that provides competitive risk-adjusted performance compared with a simple Buy & Hold strategy?**

To answer this question, the project evaluates three main dimensions:

- **Predictive performance:** Can the models correctly classify future market movements?
- **Robustness:** Do the model results remain reasonably consistent under time-series validation?
- **Investment performance:** Does the resulting strategy generate attractive returns while controlling risk compared with Buy & Hold?



## 4. Data Collection

The analysis is based on historical market data for Amazon (AMZN), with the S&P 500 used as a broader market benchmark.

The raw Amazon market data was first collected and stored separately from the processed dataset. The project then applies a data-preparation workflow to produce a clean dataset suitable for statistical analysis and machine-learning modelling.

The project contains the following main market-data files:

- `amzn_market_raw.csv` — raw Amazon market data.
- `amzn_market_clean.csv` — cleaned Amazon market data used for analysis.
- `sp500_market_clean.csv` — cleaned S&P 500 benchmark data.
- `amzn_ml_strategy_results.csv` — results generated from the machine-learning investment strategy.
- `model_performance_summary.csv` — summary of model-performance results.

The data-processing workflow is designed to maintain a clear separation between raw inputs and processed analytical datasets. This makes the analysis easier to reproduce and reduces the risk of unintentionally modifying the original data.

The cleaned datasets are subsequently used across the statistical-analysis and machine-learning stages of the project. The Amazon dataset provides the primary asset information, while the S&P 500 provides a market-level reference for evaluating Amazon's performance in a broader context.


## 5. Data Preparation

Before conducting the statistical and machine-learning analysis, the raw market data was cleaned and prepared for modelling.

The preparation process included converting the date information into a consistent date format, organizing the observations chronologically, and ensuring that the datasets were suitable for subsequent calculations and modelling.

Separate cleaned datasets were maintained for Amazon and the S&P 500. The Amazon dataset was used as the primary source for the machine-learning strategy, while the S&P 500 dataset was retained as a benchmark for broader market comparison.

The cleaned Amazon data was then used to construct the variables required for the machine-learning stage. These variables were derived from historical market information and were used to predict the direction of future price movements.

The data preparation stage was designed to avoid unnecessary modification of the original observations while creating a consistent analytical dataset. Keeping the raw and processed data separate also improves reproducibility and makes it easier to trace the analysis back to the original source data.

The prepared datasets were subsequently used for statistical analysis, machine-learning model development, strategy construction, and historical backtesting.


## 6. Statistical Analysis

The statistical analysis was conducted to evaluate Amazon's historical return, risk, volatility, and relationship with the broader market.

For Amazon (AMZN), the analysis produced an annualized mean return of approximately 22.92% and annualized volatility of 34.41%. The resulting Sharpe ratio was 0.67, while the maximum drawdown was -56.15%.

For comparison, the S&P 500 produced an annualized mean return of approximately 13.61%, annualized volatility of 19.60%, and a Sharpe ratio of 0.69. Its maximum drawdown was -33.93%.

The results indicate that Amazon generated a higher historical return than the S&P 500 over the analysed period, but this was accompanied by substantially higher volatility and a deeper maximum drawdown. The similar Sharpe ratios suggest that the additional return was associated with a correspondingly higher level of risk.

The relationship between Amazon and the S&P 500 was also examined. The correlation coefficient was approximately 0.67, indicating a moderately strong positive relationship between Amazon and the broader market. Amazon's estimated beta was approximately 1.18, suggesting that the stock historically exhibited greater sensitivity to market movements than the S&P 500.

Rolling volatility and drawdown analysis provided additional evidence of Amazon's changing risk profile over time. Amazon generally experienced higher volatility and deeper drawdowns, particularly during periods of significant market stress.

Overall, the statistical analysis highlights the trade-off between return and risk in Amazon's historical performance. These findings provide an important foundation for the subsequent machine-learning and investment-strategy analysis.


## 7. Machine-Learning Methodology

The machine-learning stage was designed to investigate whether historical market information could be used to predict the future direction of Amazon (AMZN) stock returns.

The problem was formulated as a binary classification task. The target variable represents the direction of the next-period price movement, with the model predicting whether the future return would be positive or negative.

Two classification models were implemented: Logistic Regression and Random Forest. These models were selected because they provide complementary approaches to the prediction problem.

Logistic Regression was used as a relatively simple and interpretable baseline model. It estimates the probability of an upward price movement based on the explanatory variables. Its coefficients also provide an indication of how the selected features are associated with the predicted direction.

Random Forest was used as a non-linear ensemble model. It combines multiple decision trees and can capture more complex relationships between the input variables and the target. This provides a useful comparison with the simpler Logistic Regression approach.

The explanatory variables were constructed from historical market information available at the time of prediction. The modelling process was designed to preserve the chronological structure of the financial data and avoid using future observations to predict the past.

The dataset was divided into training and testing samples using a chronological train-test split rather than a random split. The models were therefore trained using earlier observations and evaluated on subsequent observations. This approach is more appropriate for financial time-series data because randomly mixing observations could introduce look-ahead bias.

Both models were evaluated using classification performance measures, including accuracy and classification reports. ROC-AUC was also calculated to provide an additional measure of the models' ability to distinguish between positive and negative future price movements.

The machine-learning results were subsequently used as the foundation for the investment-strategy stage. Model predictions were converted into trading signals, which were then evaluated through historical backtesting and compared with a simple Buy & Hold strategy.


## 8. Model Evaluation

The performance of the machine-learning models was evaluated using out-of-sample test data. Several classification metrics were considered in order to assess whether the models could reliably distinguish between positive and negative future price movements.

### 8.1 Logistic Regression

The Logistic Regression model achieved an accuracy of approximately 53.27% on the initial test set. Its ROC-AUC score was approximately 0.5501, indicating only a modest ability to distinguish between the two classes.

The confusion matrix showed that the model classified all 398 test observations as the positive class. Although this resulted in an accuracy slightly above 50%, the confusion matrix indicates that the model did not effectively distinguish between positive and negative observations.

This highlights an important limitation of relying on accuracy alone. A model can achieve an apparently reasonable accuracy while providing limited practical predictive value if it is biased toward one class.

### 8.2 Random Forest

The Random Forest model achieved an accuracy of approximately 48.74%, which was below the performance of the Logistic Regression model.

Its ROC-AUC score was approximately 0.4923, which is very close to 0.50. This indicates that the model had little ability to distinguish between positive and negative future price movements on the test data.

The Random Forest confusion matrix was:

| | Predicted Negative | Predicted Positive |
|---|---:|---:|
| Actual Negative | 84 | 102 |
| Actual Positive | 102 | 110 |

The relatively balanced errors across the two classes indicate that the model did not identify a strong predictive pattern in the test period.

### 8.3 Interpretation

Overall, neither model demonstrated strong predictive performance. Logistic Regression performed slightly better than Random Forest according to both accuracy and ROC-AUC, but its ROC-AUC of 0.5501 still indicates only weak predictive discrimination.

The Random Forest ROC-AUC of 0.4923 was effectively consistent with random classification performance.

These results suggest that the historical features used in the analysis contained limited information about the direction of future Amazon returns. Consequently, the machine-learning models should not be interpreted as reliable standalone forecasting systems.

The predictive results were therefore followed by robustness testing and investment backtesting. This allowed the analysis to determine whether the model predictions could nevertheless produce a meaningful investment strategy when converted into trading signals.


## 9. Robustness Testing

A single train-test split can provide an incomplete view of machine-learning performance, particularly when working with financial time-series data. To assess whether the model results were reasonably stable across different periods, a time-series cross-validation procedure was performed.

The analysis used a five-fold Time Series Split. Unlike conventional random cross-validation, this approach preserves the chronological order of the observations. In each successive fold, the models were trained using earlier observations and evaluated on a later period.

This methodology is particularly important for financial applications because information from the future should never be used when predicting an earlier observation. Preserving the temporal structure therefore provides a more realistic assessment of how the models might perform on unseen market data.

Time-series cross-validation was applied to both the Logistic Regression and Random Forest models. The resulting cross-validation scores were examined across the different folds to determine whether model performance remained reasonably consistent or varied substantially between periods.

The robustness analysis showed that model performance was not consistently strong across the different time periods. This provides additional evidence that the predictive relationships identified by the models were relatively weak and may not remain stable across changing market conditions.

These findings are important when interpreting the machine-learning results. Even when a model performs reasonably well on a particular test period, inconsistent performance across different historical periods reduces confidence that the model captures a stable and generalisable relationship.

Overall, the robustness testing supports a cautious interpretation of the predictive results. The models may contain some useful information for generating investment signals, but the evidence is not strong enough to conclude that their predictive performance is stable across different market environments.

The analysis therefore proceeds beyond predictive metrics and evaluates whether the model-generated signals have practical investment value through historical backtesting.


## 10. Investment Strategy Backtest

To evaluate whether the machine-learning predictions could have practical investment value, the Logistic Regression predictions were converted into a simple systematic investment strategy.

The trading signal was based on the predicted direction of the next-period Amazon return. When the model predicted a positive price movement, the strategy took a long position in Amazon. When the model predicted a negative movement, the strategy remained in cash.

The strategy return for each period was calculated by multiplying the trading signal by the subsequent Amazon return. This ensured that the investment strategy used the model prediction to determine exposure to the following period rather than using information from the future.

The cumulative strategy performance was then calculated by compounding the individual strategy returns over time.

For comparison, a simple Buy & Hold benchmark was constructed. Under this approach, the investor remained continuously invested in Amazon throughout the backtest period, regardless of the model predictions.

The backtest produced a positive total return for the machine-learning strategy. The strategy generated a total return of approximately **11.32%**, compared with **28.72%** for the Buy & Hold benchmark.

Although the machine-learning strategy generated a positive result, it therefore underperformed the passive Buy & Hold approach in terms of total return.

The backtest demonstrates that predictive accuracy alone does not necessarily translate into superior investment performance. Trading decisions, periods of market exposure and the distribution of returns across time can have a substantial effect on the final investment outcome.

The strategy performance was therefore evaluated using additional risk-adjusted measures, including annualized return, volatility, Sharpe ratio and maximum drawdown. These measures provide a more complete assessment of the trade-off between return and risk.


## 11. Investment Performance Evaluation

The machine-learning strategy was evaluated using several investment-performance measures in order to assess both its return potential and its associated risk.

The backtest showed that the machine-learning strategy generated a positive return over the evaluation period. However, its total return was lower than that of the Buy & Hold benchmark, indicating that the predictive strategy did not generate superior absolute performance during the tested period.

In terms of risk, the machine-learning strategy exhibited lower volatility than the Buy & Hold approach. This indicates that the strategy reduced the variability of portfolio returns by remaining in cash during periods when the model predicted a negative price movement.

The strategy also produced a smaller maximum drawdown than Buy & Hold. Maximum drawdown measures the largest decline from a previous portfolio peak and is an important indicator of downside risk. The lower drawdown suggests that the machine-learning strategy provided some degree of downside-risk reduction during the backtest period.

The Sharpe ratio was also considered to evaluate the relationship between return and volatility. Although the machine-learning strategy did not outperform Buy & Hold in absolute return, its lower volatility and smaller drawdown indicate a more conservative risk profile.

Overall, the results highlight an important trade-off between return and risk. The machine-learning strategy did not outperform a simple passive investment strategy in terms of total or annualized return, but it reduced portfolio volatility and maximum drawdown.

These findings suggest that the machine-learning approach may have some value as a risk-management or signal-generation tool. However, the results do not provide sufficient evidence that the strategy is superior to Buy & Hold as a standalone investment approach.

The performance evaluation should also be interpreted within the limitations of historical backtesting. Past market behaviour does not guarantee future performance, and transaction costs, taxes, liquidity constraints and changing market conditions could affect the results of a real-world implementation.


## 12. Final Conclusion

This project investigated whether machine-learning techniques could be used to develop an investment strategy for Amazon (AMZN) stock.

The analysis followed a complete quantitative-investment workflow, beginning with financial-data collection and preparation, followed by statistical analysis, machine-learning modelling, model evaluation, robustness testing and historical backtesting. The machine-learning stage focused on two classification approaches: Logistic Regression and Random Forest.

The statistical analysis showed that Amazon historically generated a higher return than the S&P 500 over the analysed period, but this higher return was accompanied by substantially greater volatility and a deeper maximum drawdown. The relationship between Amazon and the broader market was also examined through correlation and beta analysis.

The machine-learning models were evaluated using out-of-sample test data and several classification metrics, including accuracy and ROC-AUC. Time-series cross-validation was additionally applied to reduce the risk of obtaining misleading results from a single train-test split.

The results indicate that the machine-learning models provided limited predictive value for forecasting the direction of Amazon's next-period return. In particular, the model performance was not sufficiently strong to demonstrate reliable predictive superiority over a simple baseline.

The investment backtest produced a positive return for the machine-learning strategy, but the strategy underperformed the Buy & Hold benchmark in terms of total and annualized return. The Buy & Hold strategy generated a higher return over the tested period, while the machine-learning strategy exhibited lower volatility and a smaller maximum drawdown.

These findings highlight an important distinction between predictive performance and investment performance. A model does not necessarily need to achieve strong classification results to reduce portfolio risk, but lower risk does not automatically imply superior investment performance.

Overall, the results do not provide sufficient evidence that the tested machine-learning strategy should replace a passive Buy & Hold approach for Amazon. However, the strategy may have potential as an experimental signal-generation or risk-management tool.

The conclusions should be interpreted with caution because the analysis is based on historical market data. Financial markets are dynamic, and relationships observed in the historical sample may not remain stable in the future. Further research could improve the analysis by testing additional features, alternative machine-learning algorithms, different time periods and more sophisticated portfolio-management techniques. Transaction costs, trading frictions and other real-world implementation constraints should also be incorporated into future versions of the strategy.

Despite these limitations, the project demonstrates a complete quantitative-investment research process, combining financial data analysis, statistical methods, machine learning, time-series validation and investment backtesting. It therefore provides a practical foundation for further quantitative-finance research and development.