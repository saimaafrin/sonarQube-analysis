
import os
import shutil
import glob

def task_func(src_dir, dest_dir, ext):
    if not os.path.exists(src_dir) or not os.path.exists(dest_dir):
        raise FileNotFoundError("Source or destination directory does not exist")
    files = glob.glob(src_dir + "/*." + ext)
    moved_files = []
    for file in files:
        if not os.path.exists(dest_dir + "/" + os.path.basename(file)):
            shutil.move(file, dest_dir)
            moved_files.append(file)
    return moved_files