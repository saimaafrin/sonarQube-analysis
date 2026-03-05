import os
import logging
def task_func(directory):
    # Set up logging configuration
    logging.basicConfig(filename='jquery_removal.log', level=logging.INFO)
    
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    
    removed_files = []
    file_count = 0
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file name contains 'jquery'
            if 'jquery' in file.lower():
                file_path = os.path.join(root, file)
                # Remove the file
                os.remove(file_path)
                removed_files.append(file)
                file_count += 1
                # Log the removed file
                logging.info(f"Removed file: {file_path}")
    
    return file_count, removed_files