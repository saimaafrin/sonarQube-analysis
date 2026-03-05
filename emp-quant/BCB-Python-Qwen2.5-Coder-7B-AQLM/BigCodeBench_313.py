
import re
import os
import shutil
from datetime import datetime

def task_func(directory):
    # Initialize the dictionary to store the results
    result_dict = {}
    
    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if the file is a regular file
        if os.path.isfile(file_path):
            # Use regular expression to find the first text not enclosed in square brackets
            match = re.search(r'(?<!\[)[^[]+', filename)
            
            if match:
                # Get the text that is not enclosed in square brackets
                subdir_name = match.group(0)
                
                # Create the subdirectory if it does not exist
                subdir_path = os.path.join(directory, subdir_name)
                if not os.path.exists(subdir_path):
                    os.makedirs(subdir_path)
                
                # Move the file to the subdirectory
                shutil.move(file_path, os.path.join(subdir_path, filename))
                
                # Add the file to the dictionary
                if subdir_name not in result_dict:
                    result_dict[subdir_name] = []
                result_dict[subdir_name].append(filename)
    
    # Return the directory path and the dictionary of moved files
    return directory, result_dict