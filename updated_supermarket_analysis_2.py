import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up styles
sns.set(style='white', palette='pastel')
plt.rcParams.update({'figure.figsize': (10, 6), 'axes.titlesize': 16})

# Load and preprocess data
df = pd.read_csv('supermarket_sales.csv')

# Convert 'Date' and 'Time' to datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time']).dt.time
df['Month'] = df['Date'].dt.month_name()
df['Day'] = df['Date'].dt.day_name()
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour

# Summary metrics
print("\n📊 Summary Statistics:")
print(f"🧾 Total Revenue: ${df['Total'].sum():,.2f}")
print(f"⭐ Average Rating: {df['Rating'].mean():.2f}")
print(f"💳 Most Common Payment Method: {df['Payment'].mode()[0]}")
print(f"🏆 Best-Selling Product Line: {df.groupby('Product line')['Total'].sum().idxmax()}")

# ==========================
# 1. Sales by Branch 🏢
# ==========================
branch_sales = df.groupby('Branch')['Total'].sum().sort_values(ascending=False)
sns.barplot(x=branch_sales.index, y=branch_sales.values, palette='cool')
plt.title('🏢 Total Sales by Branch')
for i, v in enumerate(branch_sales.values):
    plt.text(i, v + 1000, f"${v:,.0f}", ha='center')
plt.tight_layout()
plt.show()

# ==========================
# 2. Product Line Performance 📦
# ==========================
product_sales = df.groupby('Product line')['Total'].sum().sort_values()
sns.barplot(x=product_sales.values, y=product_sales.index, palette='viridis')
plt.title('📦 Sales by Product Line')
for i, v in enumerate(product_sales.values):
    plt.text(v + 2000, i, f"${v:,.0f}", va='center')
plt.tight_layout()
plt.show()

# ==========================
# 3. Payment Method 💳
# ==========================
sns.countplot(x='Payment', data=df, palette='Set2')
plt.title('💳 Payment Method Distribution')
plt.tight_layout()
plt.show()

# ==========================
# 4. Customer Type & Gender 👥
# ==========================
ct_gender = df.groupby(['Customer type', 'Gender'])['Total'].sum().unstack()
ct_gender.plot(kind='bar', stacked=True, colormap='Accent')
plt.title('👥 Sales by Customer Type & Gender')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# ==========================
# 5. Rating by Product Line ⭐
# ==========================
avg_rating = df.groupby('Product line')['Rating'].mean().sort_values()
sns.barplot(x=avg_rating.values, y=avg_rating.index, palette='coolwarm')
plt.title('⭐ Avg Rating by Product Line')
plt.xlabel('Rating')
plt.tight_layout()
plt.show()

# ==========================
# 6. Monthly Trend 📅
# ==========================
month_order = ['January', 'February', 'March']
monthly_sales = df.groupby('Month')['Total'].sum().reindex(month_order)
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o', color='darkblue')
plt.title('📅 Monthly Sales Trend')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# ==========================
# 7. Daily Trend 📆
# ==========================
daily_sales = df.groupby('Date')['Total'].sum()
sns.lineplot(x=daily_sales.index, y=daily_sales.values, color='teal')
plt.title('📆 Daily Sales Trend')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# ==========================
# 8. Hourly Sales 🕒
# ==========================
hourly_sales = df.groupby('Hour')['Total'].sum()
sns.barplot(x=hourly_sales.index, y=hourly_sales.values, palette='magma')
plt.title('🕒 Hourly Sales Distribution')
plt.xlabel('Hour of Day')
plt.tight_layout()
plt.show()

# ==========================
# 9. Top 10 Invoices 💰
# ==========================
top_invoices = df.groupby('Invoice ID')['Total'].sum().nlargest(10)
sns.barplot(x=top_invoices.values, y=top_invoices.index, palette='rocket')
plt.title('💰 Top 10 Invoices by Total Spend')
plt.xlabel('Total ($)')
plt.ylabel('Invoice ID')
plt.tight_layout()
plt.show()

# ==========================
# 10. Correlation Matrix 🔗
# ==========================
corr = df[['Unit price', 'Quantity', 'Tax 5%', 'Total', 'Rating']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('🔗 Correlation Heatmap')
plt.tight_layout()
plt.show()

# ==========================
# 11. Weekday & Hour Heatmap 🔥
# ==========================
heat_df = df.groupby(['Day', 'Hour'])['Total'].sum().unstack()
heat_df = heat_df.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
sns.heatmap(heat_df, cmap='YlOrBr')
plt.title('🔥 Sales Heatmap by Day & Hour')
plt.xlabel('Hour')
plt.ylabel('Day of Week')
plt.tight_layout()
plt.show()

# ==========================
# 12. Sales by City 🌍
# ==========================
city_sales = df.groupby('City')['Total'].sum().sort_values(ascending=False)
sns.barplot(x=city_sales.values, y=city_sales.index, palette='cubehelix')
plt.title('🌍 Total Sales by City')
plt.xlabel('Sales')
plt.tight_layout()
plt.show()
