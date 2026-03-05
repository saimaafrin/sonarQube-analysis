import xlwt
import os
FIELDS = ['ID', 'Name', 'Age']
def task_func(values, filename):
    # Create an Excel file with no data
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('Sheet1')

    # Define column widths
    worksheet.col(0).width = 1000
    worksheet.col(1).width = 2500
    worksheet.col(2).width = 1500

    # Write column headers
    for i, field in enumerate(FIELDS):
        worksheet.write(0, i, field)

    # Write data
    for i, row in enumerate(values):
        for j, (key, value) in enumerate(row.items()):
            worksheet.write(i + 1, j, value)

    # Save the Excel file
    workbook.save(filename)

    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)
empty_data = []