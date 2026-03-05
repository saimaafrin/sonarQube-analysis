
import os
import logging

def task_func(directory):
    # Set up logging configuration
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
            # Check if the file contains 'jquery' in its name
            if 'jquery' in file.lower():
                # Construct the full file path
                file_path = os.path.join(root, file)
                # Remove the file
                os.remove(file_path)
                # Log the removed file
                logging.info(f"Removed file: {file_path}")
                # Increment the count and add the file name to the list
                removed_count += 1
                removed_files.append(file)
    
    # Return the result as a tuple
    return removed_count, removed_files