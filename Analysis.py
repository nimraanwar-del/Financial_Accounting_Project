import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("--- Data Analysis for Financial_Accounting_Project ---")

try:
    df = pd.read_csv('IoT_Financial_Management_Dataset.csv')
    print("✅ Data is successfully loaded!\n")
except FileNotFoundError:
    print("❌ Error: In CSV file error auccuring . Please reload your file.")
    exit()



print("first 5 rows of datasets:")
print(df.head())


print("\n--- Basic Financial Summary ---")
print(df[['Revenue', 'Operating_Cost', 'Net_Profit']].describe())

# 4. Correlation Analysis (Heatmap)
numeric_cols = df[['Revenue', 'Operating_Cost', 'Net_Profit', 'Gross_Margin', 'ROI', 'Automation_Efficiency']]
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Analysis - Financial Accounting Project')
plt.show()

# 5. Department-wise Expense Breakdown (Bar Chart)
dept_cost = df.groupby('Department')['Operating_Cost'].sum().reset_index()
dept_cost = dept_cost.sort_values(by='Operating_Cost', ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x='Operating_Cost', y='Department', data=dept_cost, palette='viridis')
plt.title('Department-wise Operating Cost Analysis')
plt.xlabel('Operating Cost ($)')
plt.ylabel('Department')
plt.show()


