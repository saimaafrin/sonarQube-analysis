import os
import shutil
def task_func(src_dir, dest_dir, extension):
    """
    Move all files with a particular extension from one directory to another.
    """
    files_moved = 0
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(extension):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)
                shutil.move(src_file, dest_file)
                files_moved += 1
    return files_moved
src_dir = "src"
dest_dir = "dest"
extension = ".txt"