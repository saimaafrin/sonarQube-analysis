
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
    
    # Raise error if no CSV files found
    if not csv_files:
        raise ValueError("No CSV files found in the specified directory.")
    
    # Initialize the Texttable object
    table = Texttable()
    headers = ["File Name", "Number of Rows", "Number of Columns"]
    table.add_row(headers)
    
    # Process each CSV file
    for file_path in csv_files:
        try:
            # Read the CSV file
            df = pd.read_csv(file_path)
            
            # Skip empty DataFrame
            if df.empty:
                raise pd.errors.EmptyDataError(f"Empty CSV file encountered: {file_path}")
            
            # Get the number of rows and columns
            num_rows = len(df)
            num_columns = len(df.columns)
            
            # Add row to the table
            table.add_row([os.path.basename(file_path), num_rows, num_columns])
        
        except pd.errors.EmptyDataError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred while processing {file_path}: {e}")
    
    # Return the string representation of the table
    return table.draw()