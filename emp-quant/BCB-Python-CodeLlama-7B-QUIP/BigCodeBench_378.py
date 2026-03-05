
import pandas as pd
from texttable import Texttable
import os
import glob

def task_func(data_dir='./data/'):
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Directory {data_dir} does not exist")
    files = glob.glob(data_dir + '*.csv')
    if len(files) == 0:
        raise ValueError("No CSV files found in directory")
    table = Texttable()
    for file in files:
        try:
            df = pd.read_csv(file)
            table.add_rows(f"{file}: {df.shape[0]} rows, {df.shape[1]} columns")
        except pd.errors.EmptyDataError:
            raise pd.errors.EmptyDataError(f"Empty CSV file: {file}")
    return table.to_string()