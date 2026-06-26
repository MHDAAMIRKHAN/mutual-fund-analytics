import pandas as pd
df = pd.read_csv("data/raw/07_scheme_performance.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())

print(df.duplicated().sum())
df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Scheme file cleaned and saved")