
import xlwt
import os

# Constants
FIELDS = ['ID', 'Name', 'Age']

def task_func(values, filename):
    # Create a new workbook
    workbook = xlwt.Workbook()
    
    # Add a sheet to the workbook
    worksheet = workbook.add_sheet('Sheet1')
    
    # Write the field names as headers
    for col_num, field_name in enumerate(FIELDS):
        worksheet.write(0, col_num, field_name)
    
    # Save the workbook to the specified file
    workbook.save(filename)
    
    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)