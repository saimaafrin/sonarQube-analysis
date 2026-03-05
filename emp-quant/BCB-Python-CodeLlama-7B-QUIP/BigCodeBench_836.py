
import os
import shutil
import csv

def task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=False):
    result = {}
    for file in os.listdir(csv_dir):
        with open(os.path.join(csv_dir, file), 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if row[0] == target_value:
                    result[file] = i
                    if not simulate:
                        shutil.move(os.path.join(csv_dir, file), os.path.join(processed_dir, file))
    return result