import xlwt
import os
FIELDS = ['ID', 'Name', 'Age']
def task_func(values, filename):
    # Create a new workbook and add a sheet
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Sheet1')
    
    # Write the column headers
    for col_idx, field in enumerate(FIELDS):
        sheet.write(0, col_idx, field)
    
    # Save the workbook to the specified file
    workbook.save(filename)
    
    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)
empty_data = []