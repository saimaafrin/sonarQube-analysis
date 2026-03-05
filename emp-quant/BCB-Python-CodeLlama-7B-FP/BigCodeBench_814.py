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
            if re.match(file_pattern, file):
                # Add the file path to the list
                file_paths.append(os.path.join(root, file))

    # Write the file paths to a configuration file
    with open(os.path.join(target_dir, 'config.txt'), 'w') as f:
        for file_path in file_paths:
            f.write(file_path + '\n')

    # Return the path to the created configuration file
    return os.path.join(target_dir, 'config.txt')
source_dir = 'C:\\SomeDir'
target_dir = 'C:\\SomeDir\\config'
file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'