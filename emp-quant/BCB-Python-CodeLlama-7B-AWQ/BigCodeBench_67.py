import pandas as pd
import re
import os
def task_func(dir_path: str, pattern: str = '^EMP'):
    """
    Look for all ascendingly sorted files in a directory that start with a given pattern, and return the number of files against their size.
    :param dir_path: The path to the directory to search in.
    :param pattern: The pattern to match against the file names.
    :return: A pandas DataFrame with file names and their sizes.
    """
    # Create a list to store the file names and sizes
    file_names = []
    file_sizes = []

    # Iterate over the files in the directory
    for file in os.listdir(dir_path):
        # Check if the file name matches the pattern
        if re.match(pattern, file):
            # Add the file name and size to the list
            file_names.append(file)
            file_sizes.append(os.path.getsize(os.path.join(dir_path, file)))

    # Create a pandas DataFrame with the file names and sizes
    df = pd.DataFrame({'File': file_names, 'Size': file_sizes})

    # Sort the DataFrame by file size
    df.sort_values(by='Size', inplace=True)

    # Return the sorted DataFrame
    return df
dir_path = 'path/to/directory'
pattern = '^EMP'