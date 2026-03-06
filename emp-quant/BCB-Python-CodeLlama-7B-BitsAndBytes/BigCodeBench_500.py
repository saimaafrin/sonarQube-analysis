
import xlwt
import os

# Constants
FIELDS = ['ID', 'Name', 'Age']

def task_func(values, filename):
    # Create an empty workbook and worksheet
    workbook = xlwt.Workbook()
    worksheet = workbook.add_worksheet()

    # Set up the column headers
    for i, field in enumerate(FIELDS):
        worksheet.write(0, i, field)

    # Write the data to the worksheet
    for i, row in enumerate(values):
        for j, (key, value) in enumerate(row.items()):
            worksheet.write(i + 1, j, value)

    # Save the workbook to a file
    workbook.save(filename)

    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)