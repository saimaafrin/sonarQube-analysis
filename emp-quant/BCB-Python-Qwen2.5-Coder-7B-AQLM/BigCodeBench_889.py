
import os
import pandas as pd
import numpy as np

def task_func(data_dir: str, csv_file: str) -> pd.DataFrame:
    # Construct the full path to the CSV file
    csv_path = os.path.join(data_dir, csv_file)
    
    # Check if the CSV file exists
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"The file {csv_file} does not exist in the directory {data_dir}")
    
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_path)
    
    # Replace NaN values in numeric columns with the mean of the corresponding column
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
    
    return df