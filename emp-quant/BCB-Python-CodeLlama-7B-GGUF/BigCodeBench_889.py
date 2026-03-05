
import os
import pandas as pd
import numpy as np

def task_func(data_dir: str, csv_file: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame and replace the NaN values in numeric columns with the mean of the corresponding column.
    The resulting DataFrame is returned. If an empty csv is passed, an empty DataFrame is returned.
    """
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"{csv_file} does not exist")

    df = pd.read_csv(csv_file)

    # Replace NaN values in numeric columns with the mean of the corresponding column
    for col in df.select_dtypes(include=['number']).columns:
        df[col].fillna(df[col].mean(), inplace=True)

    return df