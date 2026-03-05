import pandas as pd
import os
def task_func(original_file_location="test.xlsx", new_file_location="new_test.xlsx", sheet_name="Sheet1"):
    """
    Copies data from an Excel spreadsheet into a new Excel file, then reads the new Excel file and returns its contents.
    """
    # Check if the original Excel file exists
    if not os.path.exists(original_file_location):
        raise FileNotFoundError(f"The original Excel file {original_file_location} does not exist.")

    # Check if the specified sheet exists in the workbook
    if sheet_name not in pd.read_excel(original_file_location).keys():
        raise ValueError(f"The sheet {sheet_name} does not exist in the workbook {original_file_location}.")

    # Copy the data from the original Excel file to the new Excel file
    pd.read_excel(original_file_location).to_excel(new_file_location, sheet_name=sheet_name, index=False)

    # Read the new Excel file and return its contents
    return pd.read_excel(new_file_location, sheet_name=sheet_name)
original_file_location = "test.xlsx"
new_file_location = "new_test.xlsx"
sheet_name = "Sheet1"