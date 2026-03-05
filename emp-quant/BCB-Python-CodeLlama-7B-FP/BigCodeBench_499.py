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

    # Create a new Excel worksheet
    worksheet = workbook.add_worksheet()

    # Write the CSV content into the Excel worksheet
    worksheet.write(0, 0, csv_content)

    # Save the Excel file
    file_path = os.path.join(os.getcwd(), filename)
    workbook.save(file_path)

    # Return the absolute path of the created Excel file
    return os.path.abspath(file_path)
csv_content = 'Hello'
filename = 'single_cell.xls'