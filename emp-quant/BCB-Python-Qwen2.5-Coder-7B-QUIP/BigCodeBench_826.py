
import re
import os
import shutil

def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    moved_files_count = 0

    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Iterate through all files in the source directory
    for filename in os.listdir(source_dir):
        if re.match(file_pattern, filename):
            # Construct full file paths
            source_file = os.path.join(source_dir, filename)
            target_file = os.path.join(target_dir, filename)

            # Move the file to the target directory
            shutil.move(source_file, target_file)
            moved_files_count += 1

    return moved_files_count