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

    # Get a list of all files in the directory matching the pattern
    files = glob.glob(os.path.join(directory, file_pattern))

    # Check if any files were found
    if not files:
        raise ValueError(f"No files matching pattern '{file_pattern}' found in directory '{directory}'.")

    # Initialize an empty list to store the data
    data = []

    # Loop through each file and extract the numeric data
    for file in files:
        with open(file, 'r') as f:
            # Use regular expressions to extract the numeric data
            matches = re.findall(regex, f.read())
            # Add the data to the list
            data.append((file, matches))

    # Create a Pandas DataFrame from the data
    df = pd.DataFrame(data, columns=['Filename', 'Numeric Data'])

    # Sort the DataFrame by the 'Filename' column
    df.sort_values(by='Filename', inplace=True)

    return df
directory = '.'
file_pattern = '*.txt'
regex = r'([0-9]+)'