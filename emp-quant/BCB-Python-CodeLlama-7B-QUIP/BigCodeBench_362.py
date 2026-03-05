
import pandas as pd
import os

def task_func(original_file_location="test.xlsx", new_file_location="new_test.xlsx", sheet_name="Sheet1"):
    # Check if the original file exists
    if not os.path.exists(original_file_location):
        raise FileNotFoundError("The original Excel file does not exist at the specified path")

    # Read the original Excel file
    original_file = pd.read_excel(original_file_location, sheet_name=sheet_name)

    # Create a new Excel file
    new_file = pd.ExcelFile(new_file_location)

    # Write the data to the new Excel file
    new_file.write(original_file)

    # Read the new Excel file
    new_file_data = pd.read_excel(new_file_location, sheet_name=sheet_name)

    # Return the data as a pandas DataFrame
    return new_file_data