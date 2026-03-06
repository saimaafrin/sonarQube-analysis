
import pandas as pd
import os

def task_func(data_dir: str, csv_files: list) -> pd.DataFrame:
    """
    Merge/concatenate multiple CSV files from a specified directory into a single Pandas DataFrame.
    If an empty list of files is passed, an empty DataFrame is returned.

    Parameters:
    data_dir (str): The directory containing the CSV files.
    csv_files (list): A list of CSV file names.

    Returns:
    pd.DataFrame: A pandas DataFrame with the merged data.
    """
    # Check if the data_dir exists and is a directory
    if not os.path.exists(data_dir) or not os.path.isdir(data_dir):
        raise ValueError("Data directory does not exist or is not a directory")

    # Check if the csv_files list is empty
    if not csv_files:
        return pd.DataFrame()

    # Create a list to store the data from each CSV file
    data = []

    # Loop through each CSV file and append its data to the list
    for file in csv_files:
        file_path = os.path.join(data_dir, file)
        data.append(pd.read_csv(file_path))

    # Concatenate the data from each CSV file into a single DataFrame
    return pd.concat(data, ignore_index=True)