import os
import random
import json
def task_func(directory, n):
    """
    Create n random files in a directory with json content with the key 'number' and a random integer value between 1 and 100, and then reset the cursor to the beginning of each file.

    Parameters:
    - directory (str): The directory in which to generate the files.
    - n (int): The number of files to generate.

    Returns:
    - directory (str): The directory in which the files were generated.

    Requirements:
    - os
    - random
    - json

    Example:
    >>> task_func('/path/to/directory', 1)
    '/path/to/directory'
    """
    for i in range(n):
        with open(os.path.join(directory, f'file_{i}.json'), 'w') as f:
            json.dump({'number': random.randint(1, 100)}, f)
        with open(os.path.join(directory, f'file_{i}.json'), 'r') as f:
            f.seek(0)
    return directory