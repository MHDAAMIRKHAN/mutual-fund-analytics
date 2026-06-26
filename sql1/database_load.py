import pandas as pd
import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

print("Database Connected")
nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

nav.to_sql(
    "fact_nav",
    conn,
    if_exists="replace",
    index=False
)

print("NAV Table Loaded")
investor = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

investor.to_sql(
    "fact_transactions",
    conn,
    if_exists="replace",
    index=False
)

print("Transaction Table Loaded")

scheme = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

scheme.to_sql(
    "fact_performance",
    conn,
    if_exists="replace",
    index=False
)

print("Performance Table Loaded")
conn.close()

print("Database Saved Successfully")