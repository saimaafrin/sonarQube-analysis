import re
import os
import glob
def task_func(dir_path: str) -> list:
    # Regular expression to match special characters, punctuation, and spaces
    pattern = re.compile(r'[^a-zA-Z0-9]')
    
    # List to store the new file names
    new_names = []
    
    # Iterate over all files in the specified directory
    for file_path in glob.glob(os.path.join(dir_path, '*')):
        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            # Extract the file name and extension
            file_name, file_extension = os.path.splitext(os.path.basename(file_path))
            
            # Remove special characters, punctuation, and spaces using regex
            new_name = pattern.sub('', file_name) + file_extension
            
            # Construct the new file path
            new_path = os.path.join(dir_path, new_name)
            
            # Rename the file
            os.rename(file_path, new_path)
            
            # Append the new file name to the list
            new_names.append(new_name)
    
    return new_names