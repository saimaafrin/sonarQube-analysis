import xlwt
import os
import io
import csv
def task_func(csv_content, filename):
    # Create a BytesIO object to hold the Excel file in memory
    output = io.BytesIO()
    
    # Create a new Excel workbook
    workbook = xlwt.Workbook()
    
    # Add a new sheet to the workbook
    sheet = workbook.add_sheet('Sheet1')
    
    # Write the CSV content into the first cell of the sheet
    sheet.write(0, 0, csv_content)
    
    # Save the workbook to the BytesIO object
    workbook.save(output)
    
    # Move the file pointer to the beginning of the BytesIO object
    output.seek(0)
    
    # Create a temporary file path
    temp_file_path = os.path.join(os.getcwd(), filename)
    
    # Write the content of the BytesIO object to the temporary file
    with open(temp_file_path, 'wb') as f:
        f.write(output.getvalue())
    
    # Close the BytesIO object
    output.close()
    
    # Return the absolute path of the created Excel file
    return os.path.abspath(temp_file_path)