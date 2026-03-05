import xlwt
import os
import io
import csv
def task_func(csv_content, filename):
    """
    Converts CSV content into an Excel file and saves it with the given filename.
    The function reads the CSV content, creates a new Excel workbook, writes the data into the workbook, and saves it as an Excel file.
    """
    # Create a new Excel workbook
    workbook = xlwt.Workbook()

    # Add a new worksheet to the workbook
    worksheet = workbook.add_sheet('Sheet1')

    # Write the CSV content to the worksheet
    csv_reader = csv.reader(io.StringIO(csv_content))
    for row in csv_reader:
        worksheet.write_row(row)

    # Save the workbook as an Excel file
    workbook.save(filename)

    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)
csv_content = 'Hello'
filename = 'single_cell.xls'