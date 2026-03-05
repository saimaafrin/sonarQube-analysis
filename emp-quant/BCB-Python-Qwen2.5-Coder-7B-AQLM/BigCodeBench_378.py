
import pandas as pd
from texttable import Texttable
import os
import glob

def task_func(data_dir='./data/'):
    # Check if the directory exists
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"The directory {data_dir} does not exist.")
    
    # Find all CSV files in the directory
    csv_files = glob.glob(os.path.join(data_dir, '*.csv'))
    
    # Check if there are any CSV files
    if not csv_files:
        raise ValueError(f"No CSV files found in the directory {data_dir}.")
    
    # Initialize the Texttable
    table = Texttable()
    table.set_cols_dtype(['a', 'i', 'i'])  # Column types: string, integer, integer
    table.header(['File Name', 'Number of Rows', 'Number of Columns'])
    
    # Process each CSV file
    for file in csv_files:
        try:
            # Read the CSV file
            df = pd.read_csv(file)
            
            # Check if the DataFrame is empty
            if df.empty:
                raise pd.errors.EmptyDataError(f"The file {file} is empty.")
            
            # Add a row to the table
            table.add_row([os.path.basename(file), len(df), len(df.columns)])
        
        except pd.errors.EmptyDataError as e:
            print(e)
    
    # Return the string representation of the table
    return table.draw()