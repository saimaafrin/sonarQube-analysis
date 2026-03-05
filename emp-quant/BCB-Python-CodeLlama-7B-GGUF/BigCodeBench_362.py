
import pandas as pd
import os

def task_func(original_file_location="test.xlsx", new_file_location="new_test.xlsx", sheet_name="Sheet1"):
    # Check if the original file exists
    if not os.path.exists(original_file_location):
        raise FileNotFoundError(f"File {original_file_location} does not exist")

    # Read the original Excel file
    df = pd.read_excel(original_file_location, sheet_name=sheet_name)

    # Write the DataFrame to a new Excel file
    df.to_excel(new_file_location, index=False)

    # Read the new Excel file
    new_df = pd.read_excel(new_file_location, sheet_name=sheet_name)

    # Return the DataFrame
    return new_df