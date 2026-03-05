import pandas as pd
from texttable import Texttable
import os
import glob
def task_func(data_dir='./data/'):
    # Check if the specified directory exists
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"The directory {data_dir} does not exist.")
    
    # Find all CSV files in the specified directory
    csv_files = glob.glob(os.path.join(data_dir, '*.csv'))
    
    # Check if there are any CSV files in the directory
    if not csv_files:
        raise ValueError(f"No CSV files found in the directory {data_dir}.")
    
    # Initialize a Texttable object
    table = Texttable()
    
    # Add a header to the table
    table.add_row(['File Name', 'Number of Rows', 'Number of Columns'])
    
    # Iterate over each CSV file
    for file in csv_files:
        try:
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(file)
            
            # Get the number of rows and columns in the DataFrame
            num_rows = len(df)
            num_columns = len(df.columns)
            
            # Add a row to the table with the file name, number of rows, and number of columns
            table.add_row([os.path.basename(file), num_rows, num_columns])
        except pd.errors.EmptyDataError:
            # If an empty CSV file is encountered, raise a pandas.errors.EmptyDataError
            raise pd.errors.EmptyDataError(f"The file {file} is empty.")
    
    # Return the string representation of the table
    return table.draw()