import os
import shutil
import glob
def task_func(source_dir, dest_dir, extension):
    """
    Move all files with a particular extension from one directory to another.
    """
    result = 0
    for file in glob.glob(os.path.join(source_dir, '*.' + extension)):
        shutil.move(file, dest_dir)
        result += 1
    return result
source_dir = 'source'
dest_dir = 'dest'
extension = 'txt'