
import os
import shutil

def task_func(src_dir, dest_dir, extension):
    files_moved = 0
    for filename in os.listdir(src_dir):
        if filename.endswith(extension):
            src_file = os.path.join(src_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            shutil.move(src_file, dest_file)
            files_moved += 1
    return files_moved