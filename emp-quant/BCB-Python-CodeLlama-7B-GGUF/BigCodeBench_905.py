
import os
import glob
import csv

def task_func(directory_path, file_extension='.csv'):
    data = {}
    for file in glob.glob(os.path.join(directory_path, '*' + file_extension)):
        with open(file, 'r') as f:
            reader = csv.reader(f)
            data[os.path.splitext(os.path.basename(file))[0]] = [row for row in reader]
    return data