
import os
import pandas as pd
import numpy as np

def task_func(data_dir: str, csv_file: str) -> pd.DataFrame:
    # Check if the csv file exists
    if not os.path.exists(csv_file):
        raise FileNotFoundError("CSV file does not exist")

    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Replace NaN values in numeric columns with the mean of the column
    for col in df.select_dtypes(np.number):
        df[col] = df[col].fillna(df[col].mean())

    return df