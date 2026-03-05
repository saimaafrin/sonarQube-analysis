
import pandas as pd
from texttable import Texttable
import os
import glob

def task_func(data_dir='./data/'):
    # Check if the directory exists
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Directory {data_dir} does not exist.")

    # Find all CSV files in the directory
    csv_files = glob.glob(os.path.join(data_dir, '*.csv'))
    if not csv_files:
        raise ValueError(f"No CSV files found in {data_dir}.")

    # Initialize the summary table
    summary = []
    for csv_file in csv_files:
        try:
            # Read the CSV file
            df = pd.read_csv(csv_file, header=None)
            # Append the file name, number of rows, and number of columns to the summary
            summary.append([os.path.basename(csv_file), df.shape[0], df.shape[1]])
        except pd.errors.EmptyDataError:
            raise pd.errors.EmptyDataError(f"Empty CSV file encountered: {csv_file}")

    # Create the Texttable
    t = Texttable()
    t._columns = ['File Name', 'Number of Rows', 'Number of Columns']
    t._rows = summary
    t._max_width = 20

    # Return the string representation of the table
    return t.draw()