import re
import os
import glob
import natsort
import pandas as pd
def task_func(directory='./', file_pattern='*.txt', regex=r'([0-9]+)'):
    """
    Extract numeric data from all text files matching a given pattern in a directory and compile it into a Pandas DataFrame.
    The function should raise the exception for:
        FileNotFoundError: If the specified directory does not exist.
        ValueError: If no files matching the pattern are found.
    The function should output with:
        DataFrame: A pandas DataFrame with two columns: 'Filename' and 'Numeric Data'.
        Each row represents a file and its extracted numeric data.
    """
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

    # Get all files matching the pattern
    files = glob.glob(os.path.join(directory, file_pattern))
    if not files:
        raise ValueError(f"No files matching the pattern '{file_pattern}' found in '{directory}'.")

    # Extract numeric data from each file
    data = []
    for file in files:
        with open(file, 'r') as f:
            text = f.read()
            matches = re.findall(regex, text)
            if matches:
                data.append({'Filename': file, 'Numeric Data': matches})

    # Create a Pandas DataFrame
    df = pd.DataFrame(data)

    # Sort the DataFrame by the 'Filename' column
    df = df.sort_values(by='Filename')

    return df
directory = './'
file_pattern = '*.txt'
regex = r'([0-9]+)'