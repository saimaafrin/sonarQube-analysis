import re
import os
import glob
import natsort
import pandas as pd
def task_func(directory='./', file_pattern='*.txt', regex=r'([0-9]+)'):
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    
    # Find all files matching the pattern
    files = glob.glob(os.path.join(directory, file_pattern))
    if not files:
        raise ValueError(f"No files matching the pattern {file_pattern} found in {directory}.")
    
    # Initialize a list to store the data
    data = []
    
    # Iterate over the files
    for file in natsort.natsorted(files):
        with open(file, 'r') as f:
            content = f.read()
            # Find all matches in the file content
            matches = re.findall(regex, content)
            if matches:
                # Convert matches to integers
                numeric_data = [int(match) for match in matches]
                data.append({'Filename': os.path.basename(file), 'Numeric Data': numeric_data})
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    return df