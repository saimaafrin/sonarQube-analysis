
import xlwt
import os
import io
import csv

def task_func(csv_content, filename):
    # Create a new Excel workbook
    workbook = xlwt.Workbook()
    # Create a new sheet
    worksheet = workbook.add_sheet('Sheet1')
    
    # Write the CSV content into the worksheet
    worksheet.write(0, 0, csv_content)
    
    # Save the workbook to a file
    workbook.save(filename)
    
    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)