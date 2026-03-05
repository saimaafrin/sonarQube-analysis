
import pandas as pd
import os
import glob

def task_func(my_list, file_dir='./data_files/', file_ext='.csv'):
    """
    Modify a list by adding the element '12', then concatenate a number of CSV files from a directory into a single DataFrame.
    The number of files concatenated is determined by the sum of the numbers in the list.
    """
    if not isinstance(my_list, list):
        raise TypeError("'my_list' must be a list")

    my_list.append(12)

    file_paths = []
    for num in my_list:
        file_paths.extend(glob.glob(os.path.join(file_dir, f"*{num}{file_ext}")))

    if not file_paths:
        raise FileNotFoundError("No files found in the specified directory")

    df = pd.concat([pd.read_csv(file_path) for file_path in file_paths])

    return df