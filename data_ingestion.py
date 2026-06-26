import pandas as pd
import os

folder_path = "data/raw"

for file in os.listdir(folder_path):

    if file.endswith(".csv"):

        file_path = os.path.join(folder_path, file)

        print("\n" + "="*60)
        print("FILE:", file)

        df = pd.read_csv(file_path)

        print("\nSHAPE:")
        print(df.shape)

        print("\nDATA TYPES:")
        print(df.dtypes)

        print("\nFIRST 5 ROWS:")
        print(df.head())

        print("="*60)