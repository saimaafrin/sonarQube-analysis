import xlwt
import os
FIELDS = ['ID', 'Name', 'Age']
def task_func(values, filename):
    # Create an Excel file with no data
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('Sheet1')
    # Set column widths
    for i, field in enumerate(FIELDS):
        worksheet.col(i).width = 10
    # Set column headers
    for i, field in enumerate(FIELDS):
        worksheet.write(0, i, field)
    # Write data to the Excel file
    for i, row in enumerate(values):
        for j, (key, value) in enumerate(row.items()):
            worksheet.write(i + 1, j, value)
    # Save the Excel file
    workbook.save(filename)
    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)
empty_data = []