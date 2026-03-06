
import os
import shutil
import glob

def task_func(source_dir, dest_dir, extension):
    """
    Moves all files with a particular extension from source_dir to dest_dir.

    Parameters:
    source_dir (str): The directory containing the files to move.
    dest_dir (str): The destination directory where files will be moved.
    extension (str): The file extension to filter files (e.g., '.txt').

    Returns:
    int: The count of files that were moved.
    """
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Construct the pattern to match files with the specified extension
    pattern = os.path.join(source_dir, f'*{extension}')

    # Find all files matching the pattern
    files_to_move = glob.glob(pattern)

    # Move each file to the destination directory
    moved_count = 0
    for file_path in files_to_move:
        try:
            shutil.move(file_path, dest_dir)
            moved_count += 1
        except Exception as e:
            print(f"Error moving {file_path}: {e}")

    return moved_count