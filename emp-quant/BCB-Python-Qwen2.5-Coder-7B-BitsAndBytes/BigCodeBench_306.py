
import os
import logging

# Set up logging configuration
logging.basicConfig(filename='jquery_removal.log', level=logging.INFO)

def task_func(directory):
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    
    removed_files = []
    count_removed = 0
    
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if 'jquery' in file.lower() and file.endswith('.js'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    removed_files.append(file)
                    count_removed += 1
                    logging.info(f"Removed file: {file_path}")
                except Exception as e:
                    logging.error(f"Error removing file {file_path}: {e}")
    
    return count_removed, removed_files