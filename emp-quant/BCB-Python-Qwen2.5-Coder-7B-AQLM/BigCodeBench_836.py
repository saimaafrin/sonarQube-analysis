
import os
import shutil
import csv

def task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=False):
    result = {}
    
    # Ensure the processed directory exists
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)
    
    # Iterate over all files in the CSV directory
    for filename in os.listdir(csv_dir):
        if filename.endswith('.csv'):
            file_path = os.path.join(csv_dir, filename)
            row_index = -1
            
            # Open the CSV file and search for the target value
            with open(file_path, mode='r', newline='') as file:
                reader = csv.reader(file)
                for index, row in enumerate(reader):
                    if row and row[0] == target_value:
                        row_index = index
                        break
            
            # Store the result
            result[filename] = row_index
            
            # If simulate is False, move the file to the processed directory
            if not simulate:
                shutil.move(file_path, os.path.join(processed_dir, filename))
    
    return result