import xlwt
import os
import pandas as pd
def task_func(json_str, filename, sheet_name="sheet1"):
    # Check if json_str is a string, bytes, or bytearray
    if not isinstance(json_str, (str, bytes, bytearray)):
        raise TypeError("json_str must be a string, bytes, or bytearray")

    try:
        # Load JSON data
        data = pd.read_json(json_str)
    except ValueError as e:
        raise ValueError("Invalid JSON string") from e

    # Create a temporary Excel file
    temp_filename = os.path.join(os.getcwd(), "temp.xlsx")
    data.to_excel(temp_filename, index=False, sheet_name=sheet_name)

    # Rename the temporary file to the desired filename
    os.rename(temp_filename, filename)

    return os.path.abspath(filename)