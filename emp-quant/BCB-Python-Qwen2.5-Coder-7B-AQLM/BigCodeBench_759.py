
import os
import shutil
import fnmatch

def task_func(source_directory, destination_directory, file_pattern):
    moved_files = []
    for filename in os.listdir(source_directory):
        if fnmatch.fnmatch(filename, file_pattern):
            source_file = os.path.join(source_directory, filename)
            destination_file = os.path.join(destination_directory, filename)
            shutil.move(source_file, destination_file)
            moved_files.append(filename)
    return moved_files