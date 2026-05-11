import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plotting styles
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

# Load Data
df = pd.read_csv('supermarket_sales.csv')

# Preview Data
print("Preview of Data:\n", df.head(), "\n")
print("Basic Info:\n")
print(df.info())

# ===============================
# Data Preprocessing
# ===============================

# Convert 'Date' and 'Time' columns
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time']).dt.time  # Keep time only

# Extract features
df['Month'] = df['Date'].dt.month_name()
df['Day'] = df['Date'].dt.day_name()
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour

# ===============================
# Summary Stats
# ===============================
print("\nSummary Statistics:")
print(f"Total Revenue: ${df['Total'].sum():,.2f}")
print(f"Average Rating: {df['Rating'].mean():.2f}")
print(f"Most Common Payment Method: {df['Payment'].mode()[0]}")
print(f"Best-selling Product Line: {df.groupby('Product line')['Total'].sum().idxmax()}")

# Save summary stats
summary_df = pd.DataFrame({
    'Metric': ['Total Revenue', 'Average Rating'],
    'Value': [df['Total'].sum(), df['Rating'].mean()]
})
summary_df.to_csv('summary_statistics.csv', index=False)

# ===============================
# 1. Sales by Branch
# ===============================
branch_sales = df.groupby('Branch')['Total'].sum().sort_values(ascending=False)

sns.barplot(x=branch_sales.index, y=branch_sales.values, palette='Blues_d')
plt.title('Total Sales by Branch')
plt.xlabel('Branch')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# ===============================
# 2. Product Line Performance
# ===============================
product_sales = df.groupby('Product line')['Total'].sum().sort_values()

sns.barplot(x=product_sales.values, y=product_sales.index, palette='viridis')
plt.title('Sales by Product Line')
plt.xlabel('Total Sales')
plt.ylabel('Product Line')
plt.tight_layout()
plt.show()

# ===============================
# 3. Payment Method Distribution
# ===============================
sns.countplot(x='Payment', data=df, palette='Set2')
plt.title('Payment Method Distribution')
plt.xlabel('Payment Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# ===============================
# 4. Sales by Customer Type and Gender
# ===============================
ct_gender = df.groupby(['Customer type', 'Gender'])['Total'].sum().unstack()

ct_gender.plot(kind='bar', stacked=True, colormap='Accent')
plt.title('Sales by Customer Type and Gender')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# ===============================
# 5. Average Rating by Product Line
# ===============================
avg_rating = df.groupby('Product line')['Rating'].mean().sort_values()

sns.barplot(x=avg_rating.values, y=avg_rating.index, palette='coolwarm')
plt.title('Average Rating by Product Line')
plt.xlabel('Average Rating')
plt.tight_layout()
plt.show()

# ===============================
# 6. Monthly Sales Trend
# ===============================
months_order = ['January', 'February', 'March']
monthly_sales = df.groupby('Month')['Total'].sum().reindex(months_order)

sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o', color='darkblue')
plt.title('Monthly Sales Trend')
plt.ylabel('Sales')
plt.xlabel('Month')
plt.tight_layout()
plt.show()

# ===============================
# 7. Daily Sales Trend
# ===============================
daily_sales = df.groupby('Date')['Total'].sum()

sns.lineplot(x=daily_sales.index, y=daily_sales.values, color='teal')
plt.title('Daily Sales Trend')
plt.ylabel('Total Sales')
plt.xlabel('Date')
plt.tight_layout()
plt.show()

# ===============================
# 8. Hourly Sales Analysis
# ===============================
hourly_sales = df.groupby('Hour')['Total'].sum()

sns.barplot(x=hourly_sales.index, y=hourly_sales.values, palette='mako')
plt.title('Hourly Sales Distribution')
plt.xlabel('Hour of Day')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# ===============================
# 9. Top 10 Customers by Total Spend
# ===============================
top_customers = df.groupby('Invoice ID')['Total'].sum().nlargest(10)

sns.barplot(x=top_customers.values, y=top_customers.index, palette='rocket')
plt.title('Top 10 Invoices by Total Spend')
plt.xlabel('Total Spent')
plt.ylabel('Invoice ID')
plt.tight_layout()
plt.show()

# ===============================
# 10. Correlation Heatmap
# ===============================
corr = df[['Unit price', 'Quantity', 'Tax 5%', 'Total', 'Rating']].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()
