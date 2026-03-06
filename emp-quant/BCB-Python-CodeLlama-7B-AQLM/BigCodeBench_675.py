import os
import random
def task_func(directory, n_files):
    """
    Create n random text files in a specific directory, write a random string to each file, and then reset the cursor to the beginning of each file.

    Parameters:
    - directory (str): The directory in which to generate the files.
    - n_files (int): The number of files to generate.

    Returns:
    - directory (str): The directory in which the files were generated.

    Requirements:
    - os
    - random

    Example:
    >>> task_func('/path/to/directory', 5)
    '/path/to/directory'
    """
    for i in range(n_files):
        file_name = os.path.join(directory, 'file_{}.txt'.format(i))
        with open(file_name, 'w') as f:
            f.write(str(random.randint(0, 1000)))
        with open(file_name, 'r') as f:
            f.seek(0)
    return directory