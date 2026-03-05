
import os
import logging

def task_func(directory):
    # Set up logging
    logging.basicConfig(filename='jquery_removal.log', level=logging.INFO)
    
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist.")
    
    # Initialize a list to store the names of removed files
    removed_files = []
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if 'jquery' in filename and filename.endswith('.js'):
            # Remove the file
            os.remove(os.path.join(directory, filename))
            # Log the removal
            logging.info(f"Removed {filename}")
            # Add the filename to the list of removed files
            removed_files.append(filename)
    
    # Return the number of removed files and the list of removed files
    return (len(removed_files), removed_files)