
import os
import pandas as pd
import numpy as np

def task_func(data_dir: str, csv_file: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame and replace the NaN values in numeric columns with the mean of the corresponding column.
    The resulting DataFrame is returned. If an empty csv is passed, an empty DataFrame is returned.
    """
    # Check if the csv file exists
    if not os.path.exists(os.path.join(data_dir, csv_file)):
        raise FileNotFoundError(f"{csv_file} does not exist in {data_dir}")

    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(os.path.join(data_dir, csv_file))

    # Replace NaN values in numeric columns with the mean of the corresponding column
    for col in df.select_dtypes(include=['number']).columns:
        df[col] = df[col].fillna(df[col].mean())

    return df