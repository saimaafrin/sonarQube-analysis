import re
import os
import shutil
def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    """
    Look for files that match the pattern of the regular expression '(? <! Distillr)\\\\ AcroTray\\.exe' in the directory 'C:\\ SomeDir\\'. If found, write these file paths to a configuration file.
    """
    # Create a configuration file
    config_file = os.path.join(target_dir, 'config.txt')
    with open(config_file, 'w') as f:
        f.write('')

    # Find files that match the pattern
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if re.search(file_pattern, file):
                # Write the file path to the configuration file
                with open(config_file, 'a') as f:
                    f.write(os.path.join(root, file) + '\n')

    return config_file
source_dir = 'C:\\SomeDir'
target_dir = 'C:\\SomeDir\\config'
file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'