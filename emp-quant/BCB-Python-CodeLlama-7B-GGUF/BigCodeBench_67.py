
import pandas as pd
import re
import os

def task_func(dir_path: str, pattern: str = '^EMP'):
    """
    Look for all ascendingly sorted files in a directory that start with a given pattern, and return the number of files against their size.

    Parameters
    ----------
    dir_path : str
        Path to the directory to search in.
    pattern : str, optional
        Pattern to match against the file names. Defaults to '^EMP'.

    Returns
    -------
    pandas.DataFrame
        A pandas DataFrame with file names and their sizes.
    """
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if re.match(pattern, file):
                file_list.append((file, os.path.getsize(os.path.join(root, file))))

    return pd.DataFrame(file_list, columns=['File', 'Size'])