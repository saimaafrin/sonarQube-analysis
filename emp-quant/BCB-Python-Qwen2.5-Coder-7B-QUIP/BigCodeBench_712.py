
import os
import shutil
import glob

def task_func(source_dir, dest_dir, extension):
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Find all files with the specified extension in the source directory
    files_to_move = glob.glob(os.path.join(source_dir, f"*.{extension}"))

    # Move each file to the destination directory
    moved_count = 0
    for file_path in files_to_move:
        shutil.move(file_path, os.path.join(dest_dir, os.path.basename(file_path)))
        moved_count += 1

    return moved_count