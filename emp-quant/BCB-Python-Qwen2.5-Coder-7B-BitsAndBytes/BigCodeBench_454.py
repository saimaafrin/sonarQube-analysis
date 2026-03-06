
import os
import shutil
import glob

def task_func(src_dir, dest_dir, ext):
    # Check if source and destination directories exist
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"Source directory {src_dir} does not exist")
    if not os.path.exists(dest_dir):
        raise FileNotFoundError(f"Destination directory {dest_dir} does not exist")

    # List all files in the source directory with the specified extension
    src_files = glob.glob(os.path.join(src_dir, f"*.{ext}"))

    moved_files = []

    # Move each file to the destination directory if it doesn't already exist there
    for file_path in src_files:
        file_name = os.path.basename(file_path)
        dest_file_path = os.path.join(dest_dir, file_name)

        if not os.path.exists(dest_file_path):
            shutil.move(file_path, dest_file_path)
            moved_files.append(dest_file_path)

    return moved_files