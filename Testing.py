import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data & Check Integrity
try:
    df = pd.read_csv('supermarket_sales.csv')
    print("Data loaded successfully.\n")
except FileNotFoundError:
    print("Error: File not found. Ensure 'supermarket_sales.csv' is in the correct location.")
    exit()

# Preview Data
print(df.head())
print("\nBasic Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Convert 'Date' column to datetime & Extract Features
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Month'] = df['Date'].dt.month_name()
df['Day'] = df['Date'].dt.day_name()

# Validate Date Conversion
print("\nDate Column Validation:")
print(df[['Date', 'Month', 'Day']].head())

# ===============================
# 1. Sales Overview Validation
# ===============================
print("\nTotal Revenue: ${:.2f}".format(df['Total'].sum()))
print("Average Rating: {:.2f}".format(df['Rating'].mean()))

# Check numeric column statistics
print("\nNumerical Data Statistics:")
print(df.describe())

# ===============================
# 2. Sales by Branch
# ===============================
branch_sales = df.groupby('Branch')['Total'].sum().sort_values(ascending=False)

plt.figure(figsize=(6, 4))
sns.barplot(x=branch_sales.index, y=branch_sales.values)
plt.title('Total Sales by Branch')
plt.xlabel('Branch')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# ===============================
# 3. Product Line Performance
# ===============================
product_sales = df.groupby('Product line')['Total'].sum().sort_values()

plt.figure(figsize=(10, 6))
sns.barplot(x=product_sales.values, y=product_sales.index, palette='viridis')
plt.title('Sales by Product Line')
plt.xlabel('Total Sales')
plt.ylabel('Product Line')
plt.tight_layout()
plt.show()

# ===============================
# 4. Payment Method Distribution
# ===============================
plt.figure(figsize=(6, 4))
sns.countplot(x='Payment', data=df, palette='Set2')
plt.title('Payment Method Distribution')
plt.tight_layout()
plt.show()

# ===============================
# 5. Sales by Customer Type and Gender
# ===============================
ct_gender = df.groupby(['Customer type', 'Gender'])['Total'].sum().unstack()

ct_gender.plot(kind='bar', stacked=True, figsize=(8, 5), colormap='Accent')
plt.title('Sales by Customer Type and Gender')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# ===============================
# 6. Average Rating by Product Line
# ===============================
avg_rating = df.groupby('Product line')['Rating'].mean().sort_values()

plt.figure(figsize=(10, 5))
sns.barplot(x=avg_rating.values, y=avg_rating.index)
plt.title('Average Customer Rating by Product Line')
plt.xlabel('Average Rating')
plt.tight_layout()
plt.show()

# ===============================
# 7. Monthly Sales Trend
# ===============================
monthly_sales = df.groupby('Month')['Total'].sum().reindex(['January', 'February', 'March'])

plt.figure(figsize=(7, 5))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o')
plt.title('Monthly Sales Trend')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()
