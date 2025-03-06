import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

sns.set_theme(style="darkgrid")

data = {
    'Year': [2021, 2022, 2023, 2024],
    'Gross_Profit': [129516000, 119226000, 124295000, 143390000],
    'Gross_Profit_Margin': [34.46, 32.21, 32.49, 419.09],
    'Net_Profit': [33159000, 41381000, 33413000, 32953000],
    'Net_Profit_Margin': [8.82, 11.18, 8.74, 96.31],
    'Interest_Coverage_Ratio': [3.50, 3.98, 2.83, 2.55]
}

df = pd.DataFrame(data)

growth_data = {
    'Comparison': ['2023 vs 2022', '2022 vs 2021', '2024 vs 2023'],
    'Revenue_Growth_Rate': [3.33, -1.39, -10.56],
    'Net_Income_Growth_Rate': [-19.26, 24.79, -1.38]
}

growth_df = pd.DataFrame(growth_data)

plt.figure(figsize=(10, 6))
plt.bar(df['Year'], df['Gross_Profit'], color='skyblue')
plt.xlabel('Year')
plt.ylabel('Gross Profit')
plt.title('Gross Profit by Year')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Gross_Profit_Margin'], marker='o', linestyle='-', color='green')
plt.xlabel('Year')
plt.ylabel('Gross Profit Margin (%)')
plt.title('Gross Profit Margin Trend')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(df['Year'], df['Net_Profit'], color='lightcoral')
plt.xlabel('Year')
plt.ylabel('Net Profit')
plt.title('Net Profit by Year')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Net_Profit_Margin'], marker='o', linestyle='-', color='purple')
plt.xlabel('Year')
plt.ylabel('Net Profit Margin (%)')
plt.title('Net Profit Margin Trend')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Interest_Coverage_Ratio'], marker='o', linestyle='-', color='orange')
plt.xlabel('Year')
plt.ylabel('Interest Coverage Ratio')
plt.title('Interest Coverage Ratio Trend')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(growth_df['Comparison'], growth_df['Revenue_Growth_Rate'], color='steelblue', label='Revenue Growth Rate')
plt.bar(growth_df['Comparison'], growth_df['Net_Income_Growth_Rate'], color='salmon', label='Net Income Growth Rate')
plt.xlabel('Comparison Period')
plt.ylabel('Growth Rate (%)')
plt.title('Revenue and Net Income Growth Rates')
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()