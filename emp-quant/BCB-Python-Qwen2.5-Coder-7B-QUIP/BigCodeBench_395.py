
import re
import os
import glob
import natsort
import pandas as pd

def task_func(directory='./', file_pattern='*.txt', regex=r'([0-9]+)'):
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")
    
    # Find all files matching the pattern
    files = glob.glob(os.path.join(directory, file_pattern))
    if not files:
        raise ValueError(f"No files matching the pattern '{file_pattern}' found in directory '{directory}'.")

    # Initialize a list to store the data
    data = []

    # Process each file
    for file in files:
        with open(file, 'r') as f:
            content = f.read()
            # Extract numeric data using regex
            numbers = re.findall(regex, content)
            # Append the filename and extracted numbers to the data list
            data.append({'Filename': file, 'Numeric Data': numbers})

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Return the DataFrame
    return df