
import xlwt
import os
import io
import csv

def task_func(csv_content, filename):
    # Create a new Excel workbook
    workbook = xlwt.Workbook()

    # Create a new Excel worksheet
    worksheet = workbook.add_sheet('Sheet1')

    # Write the CSV content to the worksheet
    csv_reader = csv.reader(io.StringIO(csv_content))
    for row in csv_reader:
        worksheet.write_row(row)

    # Save the Excel file
    workbook.save(filename)

    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)