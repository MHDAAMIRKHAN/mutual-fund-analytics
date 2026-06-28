import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load NAV History
nav_df = pd.read_csv("data/raw/02_nav_history.csv")

# Load Scheme Performance
performance_df = pd.read_csv("data/raw/07_scheme_performance.csv")

print(nav_df.head())

print(performance_df.head())