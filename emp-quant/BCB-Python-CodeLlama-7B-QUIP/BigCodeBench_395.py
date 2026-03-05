
import re
import os
import glob
import natsort
import pandas as pd

def task_func(directory='./', file_pattern='*.txt', regex=r'([0-9]+)'):
    if not os.path.exists(directory):
        raise FileNotFoundError(f'Directory {directory} does not exist')
    files = glob.glob(os.path.join(directory, file_pattern))
    if len(files) == 0:
        raise ValueError('No files matching the pattern were found')
    data = []
    for file in files:
        with open(file, 'r') as f:
            contents = f.read()
        matches = re.findall(regex, contents)
        if len(matches) == 0:
            continue
        data.append((file, matches))
    return pd.DataFrame(data, columns=['Filename', 'Numeric Data'])