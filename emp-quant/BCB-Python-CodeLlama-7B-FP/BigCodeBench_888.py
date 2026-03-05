import pandas as pd
import os
def task_func(data_dir: str, csv_files: list) -> pd.DataFrame:
    """
    Merge / Concatenate multiple CSV files from a specified directory into a single Pandas DataFrame.
    If an empty list of files is passed, an empty DataFrame is returned.
    """
    if not csv_files:
        return pd.DataFrame()

    # Create a list of file paths
    file_paths = [os.path.join(data_dir, file) for file in csv_files]

    # Read the CSV files into a list of DataFrames
    dataframes = [pd.read_csv(file_path) for file_path in file_paths]

    # Concatenate the DataFrames
    merged_data = pd.concat(dataframes, ignore_index=True)

    return merged_data
data_dir = "data"
csv_files = ["file1.csv", "file2.csv", "file3.csv"]