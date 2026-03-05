
import pandas as pd
import os

def task_func(original_file_location="test.xlsx", new_file_location="new_test.xlsx", sheet_name="Sheet1"):
    try:
        # Check if the original file exists
        if not os.path.exists(original_file_location):
            raise FileNotFoundError(f"The file {original_file_location} does not exist.")
        
        # Read the original Excel file
        df = pd.read_excel(original_file_location, sheet_name=sheet_name)
        
        # Copy the data to a new Excel file
        df.to_excel(new_file_location, index=False)
        
        # Read the new Excel file
        new_df = pd.read_excel(new_file_location, sheet_name=sheet_name)
        
        return new_df

    except FileNotFoundError as e:
        raise e
    except KeyError as e:
        raise ValueError(f"The sheet {sheet_name} does not exist in the workbook.")
    except Exception as e:
        raise e