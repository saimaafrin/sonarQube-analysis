
import os
import shutil

def task_func(src_dir, dest_dir, extension):
    files_moved = 0
    for filename in os.listdir(src_dir):
        if filename.endswith(extension):
            shutil.move(os.path.join(src_dir, filename), os.path.join(dest_dir, filename))
            files_moved += 1
    return files_moved