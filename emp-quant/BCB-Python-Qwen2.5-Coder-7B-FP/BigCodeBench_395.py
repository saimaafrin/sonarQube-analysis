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
    file_paths = glob.glob(os.path.join(directory, file_pattern))
    
    # Raise ValueError if no files are found
    if not file_paths:
        raise ValueError(f"No files matching the pattern {file_pattern} found in {directory}.")
    
    # Initialize a list to store the results
    results = []
    
    # Iterate over the files
    for file_path in natsort.natsorted(file_paths):
        with open(file_path, 'r') as file:
            content = file.read()
            # Find all numeric data using regex
            numeric_data = re.findall(regex, content)
            # Convert the list of strings to integers
            numeric_data = [int(num) for num in numeric_data]
            # Append the filename and numeric data to the results list
            results.append({'Filename': os.path.basename(file_path), 'Numeric Data': numeric_data})
    
    # Create a DataFrame from the results
    df = pd.DataFrame(results)
    
    return df