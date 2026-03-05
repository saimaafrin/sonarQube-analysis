import pandas as pd
import os
def task_func(data_dir: str, csv_files: list) -> pd.DataFrame:
    """
    Merge / Concatenate multiple CSV files from a specified directory into a single Pandas DataFrame.
    If an empty list of files is passed, an empty DataFrame is returned.
    """
    # Check if the data directory exists
    if not os.path.exists(data_dir):
        raise ValueError(f"Data directory {data_dir} does not exist")

    # Check if the list of CSV files is empty
    if not csv_files:
        return pd.DataFrame()

    # Read the CSV files into a list of DataFrames
    data_frames = [pd.read_csv(os.path.join(data_dir, file)) for file in csv_files]

    # Concatenate the DataFrames into a single DataFrame
    merged_data = pd.concat(data_frames, ignore_index=True)

    # Return the merged DataFrame
    return merged_data
data_dir = "data"
csv_files = ["file1.csv", "file2.csv"]