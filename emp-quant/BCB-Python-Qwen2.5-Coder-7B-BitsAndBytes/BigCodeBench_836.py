
import os
import shutil
import csv

def task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=False):
    result = {}
    
    # Ensure the processed directory exists
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(csv_dir):
        if filename.endswith('.csv'):
            filepath = os.path.join(csv_dir, filename)
            try:
                with open(filepath, mode='r', newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    for index, row in enumerate(reader):
                        if row and row[0] == target_value:
                            result[filename] = index
                            break
            except Exception as e:
                print(f"Error processing {filename}: {e}")
        
        # Simulate moving the file if simulate is True
        if simulate:
            new_filepath = os.path.join(processed_dir, filename)
            shutil.move(filepath, new_filepath)
            print(f"Simulated move: {filepath} -> {new_filepath}")
    
    return result