import pandas as pd

# Load data
df = pd.read_csv("data/raw/online_retail.csv", encoding="ISO-8859-1")

# Convert datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Remove missing CustomerID
df = df.dropna(subset=['CustomerID'])

# Remove invalid data
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]

# Create Revenue
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Create Month
df['Month'] = df['InvoiceDate'].dt.to_period('M')

# Aggregate monthly
monthly = df.groupby('Month')['Revenue'].sum().reset_index()

# Save cleaned data
monthly.to_csv("data/processed/monthly_revenue.csv", index=False)

print("Data cleaning completed!")
