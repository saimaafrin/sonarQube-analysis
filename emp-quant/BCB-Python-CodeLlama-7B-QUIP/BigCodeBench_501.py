
import xlwt
import os
import pandas as pd

def task_func(json_str, filename, sheet_name="sheet1"):
    # Check if the input is a string
    if not isinstance(json_str, (str, bytes, bytearray)):
        raise TypeError("json_str must be a string, bytes, or bytearray")

    # Load the JSON data
    try:
        data = json.loads(json_str)
    except ValueError:
        raise ValueError("Invalid JSON data")

    # Check if the data is an empty array
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("The JSON data is an empty array")

    # Create the Excel file
    filepath = os.path.join(os.getcwd(), filename)
    with xlwt.Workbook(filepath, engine="xlsx") as workbook:
        sheet = workbook.add_sheet(sheet_name)

        # Write the data to the Excel sheet
        for row in data:
            sheet.write_row(row)

    # Return the absolute path of the created Excel file
    return filepath