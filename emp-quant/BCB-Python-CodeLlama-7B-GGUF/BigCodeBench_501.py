
import xlwt
import os
import pandas as pd

def task_func(json_str, filename, sheet_name="sheet1"):
    # Validate input
    if not isinstance(json_str, (str, bytes, bytearray)):
        raise TypeError("json_str must be a string, bytes, or bytearray")
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    if not isinstance(sheet_name, str):
        raise TypeError("sheet_name must be a string")

    # Convert JSON string to Pandas DataFrame
    try:
        df = pd.read_json(json_str)
    except ValueError:
        raise ValueError("Invalid JSON string")

    # Handle empty JSON arrays
    if df.empty:
        # Create an empty Excel file
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet(sheet_name)
        workbook.save(filename)
        return os.path.abspath(filename)

    # Write DataFrame to Excel file
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet(sheet_name)
    for i, row in df.iterrows():
        for j, cell in enumerate(row):
            worksheet.write(i, j, cell)
    workbook.save(filename)
    return os.path.abspath(filename)