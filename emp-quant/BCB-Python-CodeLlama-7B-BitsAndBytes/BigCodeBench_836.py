
import os
import shutil
import csv

def task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=False):
    result = {}
    for filename in os.listdir(csv_dir):
        if filename.endswith('.csv'):
            with open(os.path.join(csv_dir, filename), 'r') as csvfile:
                reader = csv.reader(csvfile)
                for i, row in enumerate(reader):
                    if row[0] == target_value:
                        result[filename] = i
                        if not simulate:
                            shutil.move(os.path.join(csv_dir, filename), os.path.join(processed_dir, filename))
                            break
    return result