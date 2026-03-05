
import os
import shutil
import fnmatch

def task_func(source_directory, destination_directory, file_pattern):
    files_moved = []
    for file in os.listdir(source_directory):
        if fnmatch.fnmatch(file, file_pattern):
            shutil.move(os.path.join(source_directory, file), os.path.join(destination_directory, file))
            files_moved.append(file)
    return files_moved