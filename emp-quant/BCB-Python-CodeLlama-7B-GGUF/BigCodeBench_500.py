
import xlwt
import os
# Constants
FIELDS = ['ID', 'Name', 'Age']
def task_func(values, filename):
    # Create a new Excel file
    workbook = xlwt.Workbook()
    # Add a new sheet to the workbook
    worksheet = workbook.add_sheet('Sheet1')
    # Set the column headers
    for i, field in enumerate(FIELDS):
        worksheet.write(0, i, field)
    # Write the data to the sheet
    for i, row in enumerate(values):
        for j, (key, value) in enumerate(row.items()):
            worksheet.write(i+1, j, value)
    # Save the workbook
    workbook.save(filename)
    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)