
import pandas as pd
import os

def task_func(original_file_location="test.xlsx", new_file_location="new_test.xlsx", sheet_name="Sheet1"):
    # Check if the original file exists
    if not os.path.exists(original_file_location):
        raise FileNotFoundError("The original Excel file does not exist at the specified path.")

    # Copy the data from the original Excel file to a new Excel file
    data = pd.read_excel(original_file_location, sheet_name=sheet_name)
    data.to_excel(new_file_location, index=False)

    # Read the new Excel file and return its contents
    new_data = pd.read_excel(new_file_location, sheet_name=sheet_name)
    return new_data

try:
    data = task_func(original_file_location, new_file_location, sheet_name)
    print(data)
except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print(e)