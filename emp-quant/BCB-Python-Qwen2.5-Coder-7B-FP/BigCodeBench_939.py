import re
import os
import glob
def task_func(dir_path: str) -> list:
    # List to store the new names of the files
    new_names = []
    
    # Iterate over all files in the specified directory
    for file_path in glob.glob(os.path.join(dir_path, '*')):
        # Check if the current path is a file
        if os.path.isfile(file_path):
            # Extract the file name and extension
            file_name, file_extension = os.path.splitext(os.path.basename(file_path))
            
            # Use regular expression to remove all non-alphanumeric characters
            new_file_name = re.sub(r'[^a-zA-Z0-9]', '', file_name)
            
            # Construct the new file path
            new_file_path = os.path.join(dir_path, new_file_name + file_extension)
            
            # Rename the file
            os.rename(file_path, new_file_path)
            
            # Append the new file name to the list
            new_names.append(new_file_name + file_extension)
    
    return new_names