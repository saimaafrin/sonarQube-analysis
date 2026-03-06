import pandas as pd
from texttable import Texttable
import os
import glob
def task_func(data_dir='./data/'):
    """
    Generates a summary table of all ascendingly sorted CSV files in a specified directory using Texttable. 
    If an empty CSV file is encountered, a pandas.errors.EmptyDataError is raised.

    Parameters:
    - data_dir (str): The directory to search for CSV files. Default is './data/'.

    Returns:
    - str: A string representation of the table summarizing the CSV files. Each row contains the file name, number of rows, and number of columns.

    Raises:
    - FileNotFoundError: If the specified directory does not exist.
    - ValueError: If there are no CSV files in the specified directory.
    - pandas.errors.EmptyDataError: If an empty CSV file is encountered.

    Requirements:
    - pandas
    - texttable
    - os
    - glob

    Example:
    >>> data_dir = './test_data/'
    >>> dummy_files = create_dummy_files(data_dir)
    >>> print(task_func(data_dir))
    +-----------+------+---------+
    |   File    | Rows | Columns |
    +===========+======+=========+
    | test2.csv | 10   | 4       |
    +-----------+------+---------+
    | test2.csv | 10   | 4       |
    +-----------+------+---------+
    | test1.csv | 5    | 2       |
    +-----------+------+---------+
    | test1.csv | 5    | 2       |
    +-----------+------+---------+
    >>> tear_down_dummy_files(data_dir, dummy_files)
    """
    if not os.path.exists(data_dir):
        raise FileNotFoundError('The specified directory does not exist.')
    if not os.path.isdir(data_dir):
        raise FileNotFoundError('The specified path is not a directory.')
    if not os.listdir(data_dir):
        raise ValueError('There are no CSV files in the specified directory.')
    csv_files = glob.glob(data_dir + '*.csv')
    table = Texttable()
    table.set_cols_align(['l', 'r', 'r'])
    table.set_cols_valign(['m', 'm', 'm'])
    table.set_cols_dtype(['t', 'i', 'i'])
    table.set_cols_width([10, 10, 10])
    table.set_deco(Texttable.HEADER)
    table.header(['File', 'Rows', 'Columns'])
    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
            table.add_row([csv_file, len(df), len(df.columns)])
        except pd.errors.EmptyDataError:
            raise pd.errors.EmptyDataError('An empty CSV file was encountered.')
    return table.draw()