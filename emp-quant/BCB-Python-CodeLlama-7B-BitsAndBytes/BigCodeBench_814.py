
import re
import os
import shutil

def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    # Create a list of files that match the file pattern
    file_list = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if re.search(file_pattern, file):
                file_list.append(os.path.join(root, file))

    # Write the list of files to a configuration file
    config_file = os.path.join(target_dir, 'config.txt')
    with open(config_file, 'w') as f:
        for file in file_list:
            f.write(file + '\n')

    return config_file