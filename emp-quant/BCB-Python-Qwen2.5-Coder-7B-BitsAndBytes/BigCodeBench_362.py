
import pandas as pd
import os

def task_func(original_file_location="test.xlsx", new_file_location="new_test.xlsx", sheet_name="Sheet1"):
    # Check if the original file exists
    if not os.path.exists(original_file_location):
        raise FileNotFoundError(f"The file {original_file_location} does not exist.")
    
    try:
        # Read the original Excel file
        df = pd.read_excel(original_file_location, sheet_name=sheet_name)
        
        # Copy the data to a new Excel file
        df.to_excel(new_file_location, index=False)
        
        return df
    
    except KeyError:
        raise ValueError(f"The sheet '{sheet_name}' does not exist in the workbook.")