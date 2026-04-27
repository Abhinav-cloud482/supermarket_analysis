import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv('supermarket_sales.csv')

# Preview Data
print(df.head())
print("\nBasic Info:")
print(df.info())

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract additional time-based features
df['Month'] = df['Date'].dt.month_name()
df['Day'] = df['Date'].dt.day_name()

# Sales Overview

print("\nTotal Revenue: ${:.2f}".format(df['Total'].sum()))
print("Average Rating: {:.2f}".format(df['Rating'].mean()))

# Sales by Branch

branch_sales = df.groupby('Branch')['Total'].sum().sort_values(ascending=False)

plt.figure(figsize=(6, 4))
sns.barplot(x=branch_sales.index, y=branch_sales.values)
plt.title('Total Sales by Branch')
plt.xlabel('Branch')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# Product Line Performance

product_sales = df.groupby('Product line')['Total'].sum().sort_values()

plt.figure(figsize=(10, 6))
sns.barplot(x=product_sales.values, y=product_sales.index, palette='viridis')
plt.title('Sales by Product Line')
plt.xlabel('Total Sales')
plt.ylabel('Product Line')
plt.tight_layout()
plt.show()

# Payment Method Distribution

plt.figure(figsize=(6, 4))
sns.countplot(x='Payment', data=df, palette='Set2')
plt.title('Payment Method Distribution')
plt.tight_layout()
plt.show()

# Sales by Customer Type and Gender

ct_gender = df.groupby(['Customer type', 'Gender'])['Total'].sum().unstack()

ct_gender.plot(kind='bar', stacked=True, figsize=(8, 5), colormap='Accent')
plt.title('Sales by Customer Type and Gender')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# Average Rating by Product Line

avg_rating = df.groupby('Product line')['Rating'].mean().sort_values()

plt.figure(figsize=(10, 5))
sns.barplot(x=avg_rating.values, y=avg_rating.index)
plt.title('Average Customer Rating by Product Line')
plt.xlabel('Average Rating')
plt.tight_layout()
plt.show()

#  Monthly Sales Trend

monthly_sales = df.groupby('Month')['Total'].sum().reindex(['January', 'February', 'March'])

plt.figure(figsize=(7, 5))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o')
plt.title('Monthly Sales Trend')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()
