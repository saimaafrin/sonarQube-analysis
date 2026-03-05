
import xlwt
import os
import io
import csv

def task_func(csv_content, filename):
    # Create a new Excel workbook
    workbook = xlwt.Workbook()

    # Create a new Excel worksheet
    worksheet = workbook.add_worksheet()

    # Write the data to the worksheet
    worksheet.write(0, 0, csv_content)

    # Save the workbook to a file
    workbook.save('single_cell.xls')

    # Return the absolute path of the created Excel file
    return os.path.abspath('single_cell.xls')