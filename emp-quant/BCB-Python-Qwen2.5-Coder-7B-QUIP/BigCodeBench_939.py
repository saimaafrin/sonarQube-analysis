
import re
import os
import glob

def task_func(dir_path: str) -> list:
    # Get all files in the directory
    files = glob.glob(os.path.join(dir_path, '*'))
    
    # Initialize a list to store new file names
    new_names = []
    
    # Iterate over the files
    for file in files:
        # Extract the base name and extension
        base_name, extension = os.path.splitext(os.path.basename(file))
        
        # Remove all non-alphanumeric characters
        new_name = re.sub(r'[^a-zA-Z0-9]', '', base_name)
        
        # Append the new name with the original extension
        new_name_with_extension = new_name + extension
        
        # Add the new name to the list
        new_names.append(new_name_with_extension)
    
    # Return the list of new names
    return new_names