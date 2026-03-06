
import os
import pandas as pd
import numpy as np

def task_func(data_dir: str, csv_file: str) -> pd.DataFrame:
    # Construct the full path to the CSV file
    file_path = os.path.join(data_dir, csv_file)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {csv_file} does not exist in directory {data_dir}.")
    
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Replace NaN values in numeric columns with the mean of the corresponding column
    for col in df.select_dtypes(include=[np.number]).columns:
        if df[col].isnull().any():
            df[col].fillna(df[col].mean(), inplace=True)
    
    return df