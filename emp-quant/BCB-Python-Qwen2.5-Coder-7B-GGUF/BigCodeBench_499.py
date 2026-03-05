
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
    
    # Save the workbook to a BytesIO object
    output = io.BytesIO()
    workbook.save(output)
    
    # Move the file pointer to the beginning of the BytesIO object
    output.seek(0)
    
    # Create a temporary file to save the Excel file
    temp_file_path = os.path.join(os.getcwd(), filename)
    
    # Write the BytesIO object to the temporary file
    with open(temp_file_path, 'wb') as f:
        f.write(output.read())
    
    # Close the BytesIO object
    output.close()
    
    # Return the absolute path of the created Excel file
    return os.path.abspath(temp_file_path)