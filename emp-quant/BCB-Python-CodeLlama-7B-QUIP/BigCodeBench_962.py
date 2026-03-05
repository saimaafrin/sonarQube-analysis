
import os
from pathlib import Path
import glob
import shutil

def task_func(source_directory: str, target_directory: str):
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"Source directory {source_directory} does not exist.")

    files_to_move = []
    for ext in ["txt", "docx", "xlsx", "csv"]:
        files_to_move.extend(glob.glob(f"{source_directory}/*.{ext}"))

    files_moved = 0
    for file in files_to_move:
        file_name = Path(file).stem
        if os.path.exists(os.path.join(target_directory, file_name)):
            new_file_name = f"{file_name}-{files_moved}.{ext}"
            files_moved += 1
            shutil.move(file, os.path.join(target_directory, new_file_name))

    return files_moved