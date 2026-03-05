import re
import os
import glob
import natsort
import pandas as pd
def task_func(directory='./', file_pattern='*.txt', regex=r'([0-9]+)'):
    """
    Extract numeric data from all text files matching a given pattern in a directory and compile it into a Pandas DataFrame.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

    files = glob.glob(os.path.join(directory, file_pattern))
    if not files:
        raise ValueError(f"No files matching pattern '{file_pattern}' found in directory '{directory}'.")

    data = []
    for file in files:
        with open(file, 'r') as f:
            contents = f.read()
            matches = re.findall(regex, contents)
            if matches:
                data.append((file, matches))

    df = pd.DataFrame(data, columns=['Filename', 'Numeric Data'])
    return df
directory = '.'
file_pattern = '*.txt'
regex = r'([0-9]+)'