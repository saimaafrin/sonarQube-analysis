import os
import shutil
import csv
def task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=False):
    result = {}
    for filename in os.listdir(csv_dir):
        if filename.endswith('.csv'):
            file_path = os.path.join(csv_dir, filename)
            with open(file_path, mode='r', newline='') as file:
                reader = csv.reader(file)
                for index, row in enumerate(reader):
                    if row and row[0] == target_value:
                        result[filename] = index
                        if not simulate:
                            shutil.move(file_path, os.path.join(processed_dir, filename))
                        break
    return result