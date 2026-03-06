
import re
import os
import glob

def task_func(dir_path: str) -> list:
    # Get a list of all files in the specified directory
    files = glob.glob(os.path.join(dir_path, '*'))
    
    new_names = []
    
    for file_path in files:
        # Extract the base name and extension
        base_name, ext = os.path.splitext(os.path.basename(file_path))
        
        # Remove all non-alphanumeric characters, punctuation, and spaces
        new_base_name = re.sub(r'[^a-zA-Z0-9]', '', base_name)
        
        # Create the new file path
        new_file_path = os.path.join(dir_path, new_base_name + ext)
        
        # Rename the file
        os.rename(file_path, new_file_path)
        
        # Append the new file name to the list
        new_names.append(new_file_path)
    
    return new_names