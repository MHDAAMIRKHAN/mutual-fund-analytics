import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nTOTAL ROWS AND COLUMNS")
print(df.shape)

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

print("\nCOLUMN NAMES")
print(df.columns.tolist())