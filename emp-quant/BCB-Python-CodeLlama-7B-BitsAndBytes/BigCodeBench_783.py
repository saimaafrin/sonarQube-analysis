
import os
import shutil

def task_func(src_dir, dest_dir, extension):
    files_moved = 0
    for file in os.listdir(src_dir):
        if file.endswith(extension):
            shutil.move(os.path.join(src_dir, file), os.path.join(dest_dir, file))
            files_moved += 1
    return files_moved

files_moved = task_func(src_dir, dest_dir, extension)
print(f'{files_moved} files moved.')