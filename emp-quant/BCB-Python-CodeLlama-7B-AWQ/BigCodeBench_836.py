import os
import shutil
import csv
def task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=False):
    """
    Scans a directory for CSV files, finds for each file the index of the row with the first cell equal to the target value, and optionally moves the processed files to another directory.
    The above example assumes that '332' is found at index 10 in 'file1.csv' and index 15 in 'file2.csv' and that the file moving is simulated.
    The function should output with:
        result (dict): A dictionary with file names as keys and the row indices as values where the target value was found.
    """
    result = {}
    for filename in os.listdir(csv_dir):
        with open(os.path.join(csv_dir, filename), 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if row[0] == target_value:
                    result[filename] = i
                    if not simulate:
                        shutil.move(os.path.join(csv_dir, filename), os.path.join(processed_dir, filename))
                    break
    return result