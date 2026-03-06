
import re
import os
import glob
import natsort
import pandas as pd

def task_func(directory='./', file_pattern='*.txt', regex=r'([0-9]+)'):
    """
    Extracts numeric data from all text files matching a given pattern in a directory and compiles it into a Pandas DataFrame.

    Parameters:
    - directory (str): The directory to search for files. Defaults to the current directory.
    - file_pattern (str): The pattern to match files against. Defaults to '*.txt'.
    - regex (str): The regular expression to extract numeric data. Defaults to r'([0-9]+)'.

    Returns:
    - DataFrame: A pandas DataFrame with two columns: 'Filename' and 'Numeric Data'.

    Raises:
    - FileNotFoundError: If the specified directory does not exist.
    - ValueError: If no files matching the pattern are found.
    """

    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")

    # Find all files matching the pattern
    file_paths = glob.glob(os.path.join(directory, file_pattern))
    if not file_paths:
        raise ValueError(f"No files matching the pattern '{file_pattern}' were found in the directory '{directory}'.")

    # Initialize an empty list to store the results
    results = []

    # Iterate over each file path
    for file_path in natsort.natsorted(file_paths):
        with open(file_path, 'r') as file:
            content = file.read()
            # Find all matches of the regex in the file content
            matches = re.findall(regex, content)
            if matches:
                # Join the matches into a single string separated by spaces
                numeric_data = ' '.join(matches)
                results.append({'Filename': os.path.basename(file_path), 'Numeric Data': numeric_data})

    # Create a DataFrame from the results
    df = pd.DataFrame(results)

    return df