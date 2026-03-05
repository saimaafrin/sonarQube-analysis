
import regex as re
import glob
import os
from openpyxl import load_workbook

def task_func(directory_path='./xlsx_files/'):
    # Get all Excel files in the specified directory
    excel_files = glob.glob(os.path.join(directory_path, '*.xlsx'))

    # Initialize counter for number of Excel files processed
    num_processed = 0

    # Iterate over Excel files
    for excel_file in excel_files:
        # Load Excel file using openpyxl
        wb = load_workbook(excel_file)

        # Iterate over worksheets in Excel file
        for sheet in wb.worksheets:
            # Get all cells in worksheet
            cells = sheet.values

            # Iterate over cells in worksheet
            for cell in cells:
                # Check if cell value is a string
                if isinstance(cell.value, str):
                    # Replace double quotes with double backslashes
                    cell.value = re.sub(r'"', '\\"', cell.value)

        # Save changes to Excel file
        wb.save(excel_file)

        # Increment counter for number of Excel files processed
        num_processed += 1

    # Return number of Excel files processed
    return num_processed