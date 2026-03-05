import xlwt
import os
FIELDS = ['ID', 'Name', 'Age']
def task_func(values, filename):
    # Create an empty workbook and worksheet
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('Sheet1')

    # Set up column headers
    for i, field in enumerate(FIELDS):
        worksheet.write(0, i, field)

    # Write data to the worksheet
    for i, row in enumerate(values):
        for j, (key, value) in enumerate(row.items()):
            worksheet.write(i + 1, j, value)

    # Save the workbook
    workbook.save(filename)

    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)
empty_data = []