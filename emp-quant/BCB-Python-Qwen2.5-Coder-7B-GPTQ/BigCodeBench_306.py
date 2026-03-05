import os
import logging
def task_func(directory):
    # Set up logging configuration
    logging.basicConfig(filename='jquery_removal.log', level=logging.INFO)
    
    # Check if the specified directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    
    # Initialize variables
    removed_files = []
    file_count = 0
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file name contains 'jquery'
            if 'jquery' in file:
                # Construct the full file path
                file_path = os.path.join(root, file)
                # Remove the file
                os.remove(file_path)
                # Log the removed file
                logging.info(f"Removed file: {file_path}")
                # Append the file name to the list
                removed_files.append(file)
                # Increment the file count
                file_count += 1
    
    # Return the result as a tuple
    return file_count, removed_files