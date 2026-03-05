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
    file_list = []

    # Iterate over the files in the directory
    for file in os.listdir(dir_path):
        # Check if the file name matches the pattern
        if re.match(pattern, file):
            # Get the file size
            file_size = os.path.getsize(os.path.join(dir_path, file))

            # Add the file name and size to the list
            file_list.append((file, file_size))

    # Create a pandas DataFrame from the list
    df = pd.DataFrame(file_list, columns=['File', 'Size'])

    # Sort the DataFrame by file size
    df = df.sort_values(by='Size', ascending=True)

    # Return the DataFrame
    return df
dir_path = 'path/to/directory'
pattern = '^EMP'