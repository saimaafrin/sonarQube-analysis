
import os
import shutil
import glob

def task_func(src_dir, dest_dir, ext):
    # Check if source and destination directories exist
    if not os.path.exists(src_dir) or not os.path.exists(dest_dir):
        raise FileNotFoundError("Source or destination directory does not exist")

    # Get a list of files in the source directory with the specified extension
    files = glob.glob(os.path.join(src_dir, "*" + ext))

    # Move files to destination directory, skipping if a file with the same name already exists
    moved_files = []
    for file in files:
        file_name = os.path.basename(file)
        dest_file = os.path.join(dest_dir, file_name)
        if not os.path.exists(dest_file):
            shutil.move(file, dest_file)
            moved_files.append(dest_file)

    return moved_files