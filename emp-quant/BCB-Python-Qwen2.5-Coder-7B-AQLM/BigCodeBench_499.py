
import xlwt
import os
import io
import csv

def task_func(csv_content, filename):
    # Create a new Excel workbook
    workbook = xlwt.Workbook()
    
    # Add a new sheet to the workbook
    sheet = workbook.add_sheet('Sheet1')
    
    # Write the CSV content into the sheet
    sheet.write(0, 0, csv_content)
    
    # Save the workbook to a file
    output = io.BytesIO()
    workbook.save(output)
    output.seek(0)
    
    # Write the file to disk
    with open(filename, 'wb') as f:
        f.write(output.getvalue())
    
    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)