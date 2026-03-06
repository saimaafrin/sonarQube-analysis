
import pandas as pd
import os
import glob

def task_func(my_list, file_dir='./data_files/', file_ext='.csv'):
    # Check if 'my_list' is a list
    if not isinstance(my_list, list):
        raise TypeError("'my_list' must be a list")

    # Check if any files are found in the specified directory
    if not os.path.exists(file_dir):
        raise FileNotFoundError("No files found in the specified directory")

    # Create a list of file paths
    file_paths = [os.path.join(file_dir, file_name) for file_name in my_list]

    # Concatenate the CSV files into a single DataFrame
    df = pd.concat([pd.read_csv(file_path) for file_path in file_paths])

    # Return the concatenated DataFrame
    return df