import pandas as pd
from texttable import Texttable
import os
import glob
def task_func(data_dir='./data/'):
    """
    Generates a summary table of all ascendingly sorted CSV files in a specified directory using Texttable.
    If an empty CSV file is encountered, a pandas.errors.EmptyDataError is raised.
    The function should raise the exception for:
        FileNotFoundError: If the specified directory does not exist.
        ValueError: If there are no CSV files in the specified directory.
        pandas.errors.EmptyDataError: If an empty CSV file is encountered.
    The function should output with:
        str: A string representation of the table summarizing the CSV files.
        Each row contains the file name, number of rows, and number of columns.
    """
    # Check if the specified directory exists
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Directory {data_dir} does not exist.")

    # Check if there are any CSV files in the specified directory
    csv_files = glob.glob(os.path.join(data_dir, '*.csv'))
    if not csv_files:
        raise ValueError(f"No CSV files found in {data_dir}.")

    # Create a Texttable object
    table = Texttable()

    # Add column headers
    table.add_rows([["File Name", "Number of Rows", "Number of Columns"]])

    # Iterate over CSV files and add rows to the table
    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
        except pd.errors.EmptyDataError:
            raise pd.errors.EmptyDataError(f"{csv_file} is empty.")
        table.add_rows([[csv_file, len(df), len(df.columns)]])

    # Return the table as a string
    return table.draw()
data_dir = "./data"