
import re
import os
import shutil

def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    # Create a list of files that match the file pattern
    file_list = [f for f in os.listdir(source_dir) if re.match(file_pattern, f)]

    # Create a configuration file with the list of files
    with open(target_dir + '\\' + 'configuration.txt', 'w') as f:
        for file in file_list:
            f.write(file + '\n')

    # Return the path to the created configuration file
    return target_dir + '\\' + 'configuration.txt'