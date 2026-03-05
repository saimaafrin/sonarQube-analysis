
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
    worksheet.write(0, 0, csv_content)

    # Save the Excel file
    file_path = os.path.join(os.getcwd(), filename)
    workbook.save(file_path)

    # Return the absolute path of the created Excel file
    return file_path