import re
import os
import shutil
def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    """
    Look for files that match the pattern of the regular expression '(? <! Distillr)\\\\ AcroTray\\.exe' in the directory 'C:\\ SomeDir\\'. If found, write these file paths to a configuration file.
    """
    # Create a list to store the file paths
    file_paths = []

    # Iterate over the files in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check if the file matches the pattern
            if re.search(file_pattern, file):
                # Add the file path to the list
                file_paths.append(os.path.join(root, file))

    # Create the configuration file
    config_file = os.path.join(target_dir, 'config.txt')
    with open(config_file, 'w') as f:
        for file_path in file_paths:
            f.write(file_path + '\n')

    # Return the path to the created configuration file
    return config_file
source_dir = 'C:\\SomeDir'
target_dir = 'C:\\SomeDir\\Config'
file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'