import os
import glob
import csv
def task_func(directory_path, file_extension='.csv'):
    """
    Reads all files with the specified extension in the given directory.
    Uses the filename without the extension as a key in the output dictionary.
    The value for each key is a list of rows from the file, where each row is represented as a list of values.
    """
    data = {}
    for filename in glob.glob(os.path.join(directory_path, '*' + file_extension)):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            data[os.path.splitext(os.path.basename(filename))[0]] = [row for row in reader]
    return data
directory_path = '/home/user/data'
file_extension = '.txt'