import xlwt
import os
FIELDS = ['ID', 'Name', 'Age']
def task_func(values, filename):
    # Create a new workbook
    workbook = xlwt.Workbook()
    # Add a sheet to the workbook
    sheet = workbook.add_sheet('Sheet1')
    # Write the column headers
    for idx, field in enumerate(FIELDS):
        sheet.write(0, idx, field)
    # Save the workbook to the specified file
    workbook.save(filename)
    # Return the absolute path of the created file
    return os.path.abspath(filename)