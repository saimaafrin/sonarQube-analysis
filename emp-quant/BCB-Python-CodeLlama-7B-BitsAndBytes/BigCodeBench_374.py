
import regex as re
import glob
import os
from openpyxl import load_workbook

def task_func(directory_path='./xlsx_files/'):
    # Get a list of all Excel files in the specified directory
    excel_files = glob.glob(os.path.join(directory_path, '*.xlsx'))

    # Initialize a counter for the number of Excel files processed
    num_files_processed = 0

    # Iterate over the list of Excel files
    for excel_file in excel_files:
        # Load the Excel file using openpyxl
        wb = load_workbook(excel_file)

        # Iterate over all worksheets in the Excel file
        for sheet in wb.worksheets:
            # Get the worksheet's cell values as a list of lists
            cell_values = sheet.values

            # Iterate over each cell in the worksheet
            for row in cell_values:
                # Check if the cell value is a string
                if isinstance(row[0], str):
                    # Replace all double quotes with double backslashes
                    row[0] = re.sub(r'"', '\\"', row[0])

            # Save the modified worksheet
            sheet.save(excel_file)

        # Increment the number of Excel files processed
        num_files_processed += 1

    # Return the number of Excel files processed
    return num_files_processed

# Call the task function with the specified directory path
num_files_processed = task_func('./xlsx_files/')

# Print the number of Excel files processed
print(f'Processed {num_files_processed} Excel files.')