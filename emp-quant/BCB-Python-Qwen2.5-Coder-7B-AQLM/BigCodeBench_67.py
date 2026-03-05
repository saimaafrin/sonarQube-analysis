
import pandas as pd
import re
import os

def task_func(dir_path: str, pattern: str = '^EMP'):
    # Initialize an empty list to store file names and sizes
    file_info = []
    
    # Compile the regex pattern
    regex = re.compile(pattern)
    
    # Walk through the directory
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # Check if the file name matches the pattern
            if regex.match(file):
                # Construct the full file path
                file_path = os.path.join(root, file)
                # Get the file size
                file_size = os.path.getsize(file_path)
                # Append the file name and size to the list
                file_info.append((file, file_size))
    
    # Create a pandas DataFrame from the file information
    df = pd.DataFrame(file_info, columns=['File', 'Size'])
    
    # Return the DataFrame
    return df