import xlwt
import os
import io
import csv
def task_func(csv_content, filename):
    # Create a BytesIO object to hold the Excel data
    output = io.BytesIO()
    
    # Create a new workbook
    workbook = xlwt.Workbook()
    
    # Add a sheet to the workbook
    sheet = workbook.add_sheet('Sheet1')
    
    # Write the CSV content to the sheet
    writer = csv.writer(sheet)
    writer.writerow([csv_content])
    
    # Save the workbook to the BytesIO object
    workbook.save(output)
    
    # Move the file pointer to the beginning of the BytesIO object
    output.seek(0)
    
    # Create a temporary file path
    temp_file_path = os.path.join(os.getcwd(), filename)
    
    # Save the BytesIO object to the temporary file
    with open(temp_file_path, 'wb') as f:
        f.write(output.getvalue())
    
    # Return the absolute path of the created Excel file
    return os.path.abspath(temp_file_path)