import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def create_revenue_trend_chart(data):
    plt.figure(figsize=(10, 6))
    sns.set_theme(style="darkgrid")
    sns.lineplot(x="Month", y="Revenue", data=data, marker='o')
    plt.title("Revenue Trend (Jan-Oct 2023)", fontsize=16)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Revenue ($)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()

def create_profit_trend_chart(data):
    plt.figure(figsize=(10, 6))
    sns.set_theme(style="darkgrid")
    sns.lineplot(x="Month", y="Profit", data=data, marker='o', color='green')
    plt.title("Profit Trend (Jan-Oct 2023)", fontsize=16)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Profit ($)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()

def create_profitability_ratio_chart(data):
    plt.figure(figsize=(8, 6))
    sns.set_theme(style="darkgrid")
    sns.barplot(x="Month", y="Profitability", data=data, color='skyblue')
    plt.title("Profitability Ratio (Jan-Oct 2023)", fontsize=16)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Profitability Ratio", fontsize=12)
    plt.xticks(rotation=45)
    plt.ylim(0, 1)  # Assuming profitability ratio is between 0 and 1
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()

def main():
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
        "Revenue": [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900],
        "Profit": [500, 550, 600, 650, 700, 750, 800, 850, 900, 950],
        "Profitability": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    }
    df = pd.DataFrame(data)

    create_revenue_trend_chart(df.copy())
    create_profit_trend_chart(df.copy())
    create_profitability_ratio_chart(df.copy())

if __name__ == "__main__":
    main()