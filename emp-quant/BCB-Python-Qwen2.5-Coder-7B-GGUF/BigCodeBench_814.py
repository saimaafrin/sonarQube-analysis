
import re
import os
import shutil

def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Define the path for the configuration file
    config_file_path = os.path.join(target_dir, 'config.txt')

    # Initialize a list to store matching file paths
    matching_files = []

    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check if the file name matches the pattern
            if re.search(file_pattern, file):
                # Construct the full file path
                full_file_path = os.path.join(root, file)
                # Append the full file path to the list
                matching_files.append(full_file_path)

    # Write the matching file paths to the configuration file
    with open(config_file_path, 'w') as config_file:
        for file_path in matching_files:
            config_file.write(file_path + '\n')

    # Return the path to the created configuration file
    return config_file_path