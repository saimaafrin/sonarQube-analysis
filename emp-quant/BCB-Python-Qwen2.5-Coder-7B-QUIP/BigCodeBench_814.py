
import re
import os
import shutil

def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    # Define the regular expression pattern
    pattern = re.compile(file_pattern)

    # Initialize a list to hold the file paths that match the pattern
    matching_files = []

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(source_dir):
        for file in files:
            # Check if the file matches the pattern
            if pattern.match(file):
                matching_files.append(os.path.join(root, file))

    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Define the path to the configuration file
    config_file_path = os.path.join(target_dir, 'config.txt')

    # Write the matching file paths to the configuration file
    with open(config_file_path, 'w') as config_file:
        for file_path in matching_files:
            config_file.write(file_path + '\n')

    # Return the path to the created configuration file
    return config_file_path