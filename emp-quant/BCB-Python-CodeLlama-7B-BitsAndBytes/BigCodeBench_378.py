
import pandas as pd
from texttable import Texttable
import os
import glob

def task_func(data_dir='./data/'):
    # Check if the data directory exists
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory '{data_dir}' does not exist")

    # Get a list of all CSV files in the data directory
    csv_files = glob.glob(os.path.join(data_dir, '*.csv'))

    # Check if there are any CSV files in the data directory
    if not csv_files:
        raise ValueError(f"No CSV files found in data directory '{data_dir}'")

    # Create a Texttable to store the summary information
    table = Texttable()
    table.set_cols_dtype(['t', 'i', 'i'])
    table.add_rows([
        ['File Name', 'Number of Rows', 'Number of Columns'],
    ])

    # Iterate over the CSV files and add their summary information to the table
    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
            table.add_row([
                os.path.basename(csv_file),
                df.shape[0],
                df.shape[1],
            ])
        except pd.errors.EmptyDataError:
            raise pd.errors.EmptyDataError(f"CSV file '{csv_file}' is empty")

    # Return the summary table as a string
    return table.draw()