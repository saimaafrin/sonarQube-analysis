
import os
import shutil
import glob

def task_func(source_dir, dest_dir, extension):
    # Get a list of all files in the source directory with the specified extension
    files = glob.glob(os.path.join(source_dir, '*.' + extension))

    # Move each file to the destination directory
    count = 0
    for file in files:
        shutil.move(file, os.path.join(dest_dir, os.path.basename(file)))
        count += 1

    # Return the count of files that were moved
    return count

result = task_func(source_dir, dest_dir, extension)
print(f'Moved {result} files.')