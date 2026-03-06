
import re
import os

def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    # Define the regex pattern to search for
    search_pattern = r'(?<! Distillr)\\\\ AcroTray\.exe'
    
    # Initialize an empty list to store matching file paths
    matching_files = []
    
    # Walk through the source directory and its subdirectories
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if re.search(search_pattern, file):
                # Construct the full path to the file
                file_path = os.path.join(root, file)
                # Append the file path to the list
                matching_files.append(file_path)
    
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Define the path for the configuration file
    config_file_path = os.path.join(target_dir, 'config.txt')
    
    # Write the matching file paths to the configuration file
    with open(config_file_path, 'w') as config_file:
        for file_path in matching_files:
            config_file.write(file_path + '\n')
    
    # Return the path to the created configuration file
    return config_file_path