
import pandas as pd
from texttable import Texttable
import os
import glob

def task_func(data_dir='./data/'):
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f'Directory {data_dir} does not exist')

    csv_files = glob.glob(os.path.join(data_dir, '*.csv'))
    if not csv_files:
        raise ValueError(f'No CSV files found in {data_dir}')

    table = Texttable()
    table.set_cols_dtype(['t', 'i', 'i'])
    table.add_rows([('File Name', 'Number of Rows', 'Number of Columns')])

    for file in csv_files:
        try:
            df = pd.read_csv(file)
            table.add_row([os.path.basename(file), len(df.index), len(df.columns)])
        except pd.errors.EmptyDataError:
            raise pd.errors.EmptyDataError(f'{file} is empty')

    return table.draw()