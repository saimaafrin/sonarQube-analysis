import re
import os
import shutil
def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    """
    Look for files that match the pattern of the regular expression '(? <! Distillr)\\\\ AcroTray\\.exe' in the directory 'C:\\ SomeDir\\'. If found, write these file paths to a configuration file.

    Parameters:
    - source_dir (str): The path to the source directory.
    - target_dir (str): The path to the target directory.
    - file_pattern (str, optional): The regular expression pattern that filenames must match in order
                                   to be moved. Default is r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b',
                                   which matches filenames that consist of alphanumeric characters
                                   and have extensions txt, doc, or docx.

    Returns:
    - str: Path to the created configuration file.

    Requirements:
    - re
    - os
    - shtuil

    Example:
    >>> task_func('/path/to/source', '/path/to/target')
    3
    """
    # Create a list of files that match the pattern
    file_list = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if re.search(file_pattern, file):
                file_list.append(os.path.join(root, file))

    # Create a configuration file
    config_file = os.path.join(target_dir, 'config.txt')
    with open(config_file, 'w') as f:
        for file in file_list:
            f.write(file + '\n')

    # Move the files
    for file in file_list:
        shutil.move(file, target_dir)

    return config_file