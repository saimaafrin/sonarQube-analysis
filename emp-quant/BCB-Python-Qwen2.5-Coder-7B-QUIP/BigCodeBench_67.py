
import pandas as pd
import re
import os

def task_func(dir_path: str, pattern: str = '^EMP'):
    # Initialize an empty list to store file names and their sizes
    file_sizes = []
    
    # Iterate over all files in the directory
    for filename in os.listdir(dir_path):
        # Check if the file name matches the given pattern
        if re.match(pattern, filename):
            # Get the full path of the file
            file_path = os.path.join(dir_path, filename)
            # Check if the file is a file and not a directory
            if os.path.isfile(file_path):
                # Get the size of the file
                size = os.path.getsize(file_path)
                # Append the file name and size to the list
                file_sizes.append((filename, size))
    
    # Create a pandas DataFrame from the list of file names and sizes
    df = pd.DataFrame(file_sizes, columns=['File', 'Size'])
    
    # Return the pandas DataFrame
    return df