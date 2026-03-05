
import re
import os
import glob
import natsort
import pandas as pd

def task_func(directory='./', file_pattern='*.txt', regex=r'([0-9]+)'):
    """
    Extract numeric data from all text files matching a given pattern in a directory and compile it into a Pandas DataFrame.

    Args:
        directory (str): Path to the directory containing the text files.
        file_pattern (str): Pattern to match the text files.
        regex (str): Regular expression to extract the numeric data.

    Returns:
        DataFrame: A pandas DataFrame with two columns: 'Filename' and 'Numeric Data'.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        ValueError: If no files matching the pattern are found.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f'Directory {directory} does not exist.')

    files = glob.glob(os.path.join(directory, file_pattern))
    if not files:
        raise ValueError(f'No files matching the pattern {file_pattern} found in {directory}.')

    data = []
    for file in files:
        with open(file, 'r') as f:
            contents = f.read()
            matches = re.findall(regex, contents)
            if matches:
                data.append({'Filename': file, 'Numeric Data': matches})

    return pd.DataFrame(data)