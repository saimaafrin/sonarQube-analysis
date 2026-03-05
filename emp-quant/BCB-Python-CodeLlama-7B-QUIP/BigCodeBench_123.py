
import pandas as pd
import os
import glob

def task_func(my_list, file_dir='./data_files/', file_ext='.csv'):
    if not isinstance(my_list, list):
        raise TypeError('my_list must be a list')
    if not os.path.exists(file_dir):
        raise FileNotFoundError('No files found in the specified directory')
    file_names = [file_dir + file_ext] * len(my_list)
    dfs = []
    for file_name in file_names:
        df = pd.read_csv(file_name)
        dfs.append(df)
    return pd.concat(dfs)