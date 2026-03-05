
import re
import os
import shutil

def task_func(source_dir, target_dir, file_pattern=r'(?<!Distillr)\\AcroTray\.exe'):
    """
    Look for files that match the pattern of the regular expression '(? <! Distillr)\\\\ AcroTray\\.exe' in the directory 'C:\\ SomeDir\\'. If found, write these file paths to a configuration file.
    """
    config_file_path = os.path.join(target_dir, 'config.txt')
    with open(config_file_path, 'w') as config_file:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                if re.search(file_pattern, file):
                    file_path = os.path.join(root, file)
                    config_file.write(file_path + '\n')
    return config_file_path