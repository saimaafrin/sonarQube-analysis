import pandas as pd
from texttable import Texttable
import os
import glob
def task_func(data_dir='./data/'):
    """
    Generates a summary table of all ascendingly sorted CSV files in a specified directory using Texttable.
    If an empty CSV file is encountered, a pandas.errors.EmptyDataError is raised.
    """
    # Check if the specified directory exists
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Directory {data_dir} does not exist.")

    # Check if there are any CSV files in the specified directory
    csv_files = glob.glob(os.path.join(data_dir, '*.csv'))
    if not csv_files:
        raise ValueError(f"No CSV files found in {data_dir}.")

    # Create a Texttable to store the summary data
    table = Texttable()
    table.set_cols_dtype(['t', 'i', 'i'])
    table.add_rows([
        ['File Name', 'Number of Rows', 'Number of Columns'],
    ])

    # Iterate over the CSV files and add their summary data to the table
    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
            table.add_row([
                os.path.basename(csv_file),
                df.shape[0],
                df.shape[1],
            ])
        except pd.errors.EmptyDataError:
            raise pd.errors.EmptyDataError(f"{csv_file} is empty.")

    # Return the summary table as a string
    return table.draw()
data_dir = './data/'