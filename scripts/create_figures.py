import matplotlib.pyplot as plt
from pathlib import Path


# Create output folder
output_dir = Path("report/figures")
output_dir.mkdir(parents=True, exist_ok=True)


# ============================================================
# 1. PERFORMANCE COMPARISON
# ============================================================

strategies = ["ML Strategy", "Buy & Hold"]
total_returns = [11.32, 28.72]

plt.figure(figsize=(8, 5))
bars = plt.bar(strategies, total_returns)

plt.title("Total Return: ML Strategy vs Buy & Hold")
plt.ylabel("Total Return (%)")
plt.axhline(0, linewidth=0.8)

for bar, value in zip(bars, total_returns):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value,
        f"{value:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig(output_dir / "performance_comparison.png", dpi=300)
plt.close()


# ============================================================
# 2. RISK COMPARISON
# ============================================================

metrics = ["Annualized Volatility", "Maximum Drawdown"]
ml_strategy = [20.86, 19.24]
buy_hold = [32.85, 30.88]

x = range(len(metrics))
width = 0.35

plt.figure(figsize=(9, 5))

bars1 = plt.bar(
    [i - width / 2 for i in x],
    ml_strategy,
    width,
    label="ML Strategy"
)

bars2 = plt.bar(
    [i + width / 2 for i in x],
    buy_hold,
    width,
    label="Buy & Hold"
)

plt.xticks(list(x), metrics)
plt.ylabel("Percentage (%)")
plt.title("Risk Comparison: ML Strategy vs Buy & Hold")
plt.legend()

for bar, value in zip(bars1, ml_strategy):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value,
        f"{value:.2f}%",
        ha="center",
        va="bottom"
    )

for bar, value in zip(bars2, buy_hold):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value,
        f"{value:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig(output_dir / "risk_comparison.png", dpi=300)
plt.close()


# ============================================================
# 3. MACHINE LEARNING MODEL PERFORMANCE
# ============================================================

models = ["Logistic Regression", "Random Forest"]
accuracy = [49.75, 48.74]
roc_auc = [0.5501, 0.4923]

x = range(len(models))
width = 0.35

plt.figure(figsize=(9, 5))

bars1 = plt.bar(
    [i - width / 2 for i in x],
    accuracy,
    width,
    label="Accuracy (%)"
)

bars2 = plt.bar(
    [i + width / 2 for i in x],
    [value * 100 for value in roc_auc],
    width,
    label="ROC-AUC × 100"
)

plt.xticks(list(x), models)
plt.ylabel("Score (%)")
plt.title("Machine-Learning Model Performance")
plt.legend()

for bar, value in zip(bars1, accuracy):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value,
        f"{value:.2f}%",
        ha="center",
        va="bottom"
    )

for bar, value in zip(bars2, roc_auc):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value * 100,
        f"{value:.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig(output_dir / "model_performance.png", dpi=300)
plt.close()


print("All three figures were created successfully.")
print("Saved to:")
print("report/figures/")