
import xlwt
import os

# Constants
FIELDS = ['ID', 'Name', 'Age']

def task_func(values, filename):
    # Create a new workbook
    workbook = xlwt.Workbook()
    
    # Add a sheet to the workbook
    sheet = workbook.add_sheet('Sheet1')
    
    # Write the column headers
    for idx, field in enumerate(FIELDS):
        sheet.write(0, idx, field)
    
    # Write the data rows
    for row_idx, row_data in enumerate(values, start=1):
        for col_idx, value in enumerate(row_data.values()):
            sheet.write(row_idx, col_idx, value)
    
    # Save the workbook to the specified file
    workbook.save(filename)
    
    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)