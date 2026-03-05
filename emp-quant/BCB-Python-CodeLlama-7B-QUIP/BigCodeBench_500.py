
import xlwt
import os
# Constants
FIELDS = ['ID', 'Name', 'Age']
def task_func(values, filename):
    # Create a new workbook and worksheet
    workbook = xlwt.Workbook()
    worksheet = workbook.add_worksheet()
    # Define the column names
    column_names = FIELDS
    # Define the column widths
    column_widths = [10, 20, 10]
    # Define the column formats
    column_formats = ['string', 'string', 'string']
    # Define the column alignments
    column_alignments = ['left', 'center', 'right']
    # Define the column headers
    column_headers = ['ID', 'Name', 'Age']
    # Define the column data
    column_data = values
    # Set the column widths
    for i in range(len(column_widths)):
        worksheet.col(i).width = column_widths[i]
    # Set the column formats
    for i in range(len(column_formats)):
        worksheet.col(i).number_format = column_formats[i]
    # Set the column alignments
    for i in range(len(column_alignments)):
        worksheet.col(i).align = column_alignments[i]
    # Set the column headers
    for i in range(len(column_headers)):
        worksheet.write(0, i, column_headers[i])
    # Set the column data
    for i in range(len(column_data)):
        worksheet.write(1, i, column_data[i])
    # Save the workbook
    workbook.save(filename)
    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)