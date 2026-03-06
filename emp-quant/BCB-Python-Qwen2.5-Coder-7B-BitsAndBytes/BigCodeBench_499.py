
import xlwt
import os
import io
import csv

def task_func(csv_content, filename):
    # Create a BytesIO object to hold the Excel file in memory
    excel_file = io.BytesIO()
    
    # Create a new Excel workbook
    workbook = xlwt.Workbook()
    
    # Add a sheet to the workbook
    sheet = workbook.add_sheet('Sheet1')
    
    # Write the CSV content to the first cell of the sheet
    sheet.write(0, 0, csv_content)
    
    # Save the workbook to the BytesIO object
    workbook.save(excel_file)
    
    # Move the cursor to the beginning of the BytesIO object
    excel_file.seek(0)
    
    # Get the current working directory
    current_directory = os.getcwd()
    
    # Construct the full path for the output file
    output_path = os.path.join(current_directory, filename)
    
    # Open the output file in binary write mode
    with open(output_path, 'wb') as f:
        # Write the contents of the BytesIO object to the output file
        f.write(excel_file.read())
    
    # Return the absolute path of the created Excel file
    return os.path.abspath(output_path)