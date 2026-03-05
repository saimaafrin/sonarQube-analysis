
import pandas as pd
import os

def task_func(data_dir: str, csv_files: list) -> pd.DataFrame:
    """
    Merge / Concatenate multiple CSV files from a specified directory into a single Pandas DataFrame.
    If an empty list of files is passed, an empty DataFrame is returned.
    """
    if not csv_files:
        return pd.DataFrame()

    file_paths = [os.path.join(data_dir, file) for file in csv_files]
    dfs = [pd.read_csv(file_path) for file_path in file_paths]
    return pd.concat(dfs, ignore_index=True)