import pandas as pd

# Load cleaned data
df = pd.read_csv("data/processed/monthly_revenue.csv")

# Simulate cost
df['Cost'] = df['Revenue'] * 0.6

# Create cashflow
df['Cashflow'] = df['Revenue'] - df['Cost']

# Add initial investment
df.loc[0, 'Cashflow'] = -2000

# Save
df.to_csv("data/processed/cashflow.csv", index=False)

print("Cashflow created!")
