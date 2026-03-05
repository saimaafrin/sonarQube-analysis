
import os
import logging

def task_func(directory):
    # Set up logging
    logging.basicConfig(filename='jquery_removal.log', level=logging.INFO)
    
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    
    # Initialize variables
    removed_count = 0
    removed_files = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if 'jquery' in file.lower():
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    removed_count += 1
                    removed_files.append(file)
                    logging.info(f"Removed: {file_path}")
                except Exception as e:
                    logging.error(f"Error removing {file_path}: {e}")
    
    return removed_count, removed_files