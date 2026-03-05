import os
import glob
import csv
def task_func(directory_path, file_extension='.csv'):
    """
    Reads all files with the specified extension in the given directory.
    Returns a dictionary where each key is the filename (without extension) and the value is a list of rows from the file.
    """
    data = {}
    for file in glob.glob(os.path.join(directory_path, '*' + file_extension)):
        with open(file, 'r') as f:
            reader = csv.reader(f)
            data[os.path.splitext(os.path.basename(file))[0]] = [row for row in reader]
    return data
directory_path = '/home/user/data'
file_extension = '.txt'