
import xlwt
import os
# Constants
FIELDS = ['ID', 'Name', 'Age']

def task_func(values, filename):
    # Create a new Excel workbook
    workbook = xlwt.Workbook()
    # Add a new sheet
    worksheet = workbook.add_sheet('Sheet1')
    
    # Write the column headers
    for idx, field in enumerate(FIELDS, start=1):
        worksheet.write(0, idx, field)
    
    # Save the workbook to the specified filename
    workbook.save(filename)
    
    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)