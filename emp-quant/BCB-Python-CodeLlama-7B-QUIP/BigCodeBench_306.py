
import os
import logging

def task_func(directory):
    logging.basicConfig(filename='jquery_removal.log', level=logging.INFO)
    files_removed = 0
    files_names = []
    for file in os.listdir(directory):
        if 'jquery' in file:
            os.remove(os.path.join(directory, file))
            files_removed += 1
            files_names.append(file)
    logging.info(f'Removed {files_removed} files: {files_names}')
    return files_removed, files_names