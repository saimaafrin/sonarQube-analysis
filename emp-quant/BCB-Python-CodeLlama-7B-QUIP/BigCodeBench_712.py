
import os
import shutil
import glob

def task_func(source_dir, dest_dir, extension):
    files = glob.glob(source_dir + '/*.' + extension)
    count = 0
    for file in files:
        shutil.move(file, dest_dir)
        count += 1
    return count