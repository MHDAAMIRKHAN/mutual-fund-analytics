import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print(df.head())

print(df.info())

df['date'] = pd.to_datetime(df['date'])

print(df.dtypes)
print(df.duplicated().sum())
print(df['nav'].min())
df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)
print("Clean file saved successfully")