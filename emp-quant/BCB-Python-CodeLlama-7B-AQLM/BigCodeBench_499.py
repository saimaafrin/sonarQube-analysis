import xlwt
import os
import io
import csv
def task_func(csv_content, filename):
    """
    Converts CSV content into an Excel file and saves it with the given filename. The function reads the CSV content,
    creates a new Excel workbook, writes the data into the workbook, and saves it as an Excel file.

    Parameters:
    csv_content (str): The CSV content as a string, where rows are separated by newlines and columns by commas.
    filename (str): The name of the Excel file to be created, including the .xls extension.

    Returns:
    str: The absolute path of the created Excel file.

    Requirements:
    - xlwt
    - os
    - io
    - csv

    Examples:
    Convert simple CSV content to an Excel file and return its path.
    >>> csv_content = 'ID,Name,Age\\n1,John Doe,30\\n2,Jane Doe,28'
    >>> os.path.isfile(task_func(csv_content, 'test_data.xls'))
    True

    Create an Excel file with a single cell.
    >>> csv_content = 'Hello'
    >>> os.path.isfile(task_func(csv_content, 'single_cell.xls'))
    True
    """
    # Create a new Excel workbook.
    workbook = xlwt.Workbook()

    # Create a new Excel sheet.
    worksheet = workbook.add_sheet('Sheet 1')

    # Create a CSV reader.
    csv_reader = csv.reader(io.StringIO(csv_content), delimiter=',')

    # Write the CSV content into the Excel workbook.
    row_index = 0
    for row in csv_reader:
        column_index = 0
        for cell in row:
            worksheet.write(row_index, column_index, cell)
            column_index += 1
        row_index += 1

    # Save the Excel workbook as an Excel file.
    workbook.save(filename)

    # Return the absolute path of the created Excel file.
    return os.path.abspath(filename)