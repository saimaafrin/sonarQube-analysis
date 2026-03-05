
import os
import shutil
import csv
def task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=False):
    result = {}
    for filename in os.listdir(csv_dir):
        if filename.endswith('.csv'):
            file_path = os.path.join(csv_dir, filename)
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                for i, row in enumerate(reader):
                    if row[0] == target_value:
                        result[filename] = i
                        if simulate:
                            processed_file_path = os.path.join(processed_dir, filename)
                            shutil.move(file_path, processed_file_path)
                        break
    return result