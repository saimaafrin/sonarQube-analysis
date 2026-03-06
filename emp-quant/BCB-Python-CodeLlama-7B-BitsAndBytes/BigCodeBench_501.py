
import xlwt
import os
import pandas as pd

def task_func(json_str, filename, sheet_name="sheet1"):
    # Check if the JSON string is valid
    try:
        json_data = json.loads(json_str)
    except ValueError:
        raise ValueError("Invalid JSON string")

    # Check if the JSON string represents an empty array
    if not json_data:
        # Create an Excel file with no data rows
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet(sheet_name)
        workbook.save(filename)
        return os.path.abspath(filename)

    # Convert the JSON data to a Pandas DataFrame
    df = pd.DataFrame(json_data)

    # Create an Excel file with the data
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet(sheet_name)
    for i, row in df.iterrows():
        for j, cell in enumerate(row):
            worksheet.write(i, j, cell)
    workbook.save(filename)
    return os.path.abspath(filename)