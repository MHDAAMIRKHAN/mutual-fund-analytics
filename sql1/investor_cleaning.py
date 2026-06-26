import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print(df.head())

print(df.info())
print(df.duplicated().sum())
print(df.duplicated().sum())
print(df['transaction_type'].unique())
print(df.isnull().sum())
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Investor file cleaned and saved")
print(df['amount_inr'].min())