import os
import shutil
import string
INVALID_CHARACTERS = string.punctuation + string.whitespace
def task_func(directory_path):
    """
    Scan a directory and organize the files according to their endings. Files with invalid characters in the name will be moved to a new directory called "Invalid."
    
    The invalid characters are defined by the constant INVALID_CHARACTERS, which includes all punctuation and whitespace characters.

    Parameters:
    - directory_path (str): The path to the directory.

    Returns:
    - summary (dict): A summary dictionary containing the count of files moved to each directory.

    Requirements:
    - os
    - shutil
    - string

    Example:
    >>> task_func('path_to_directory')
    {'txt': 2, 'jpg': 1, 'Invalid': 1}
    """
    summary = {}
    for ending in ['txt', 'jpg']:
        summary[ending] = 0
    invalid_dir = os.path.join(directory_path, 'Invalid')
    if not os.path.exists(invalid_dir):
        os.mkdir(invalid_dir)
    for file in os.listdir(directory_path):
        if file.endswith(ending):
            shutil.move(os.path.join(directory_path, file), os.path.join(directory_path, ending))
            summary[ending] += 1
        else:
            for char in INVALID_CHARACTERS:
                if char in file:
                    shutil.move(os.path.join(directory_path, file), os.path.join(invalid_dir, file))
                    break
    return summary