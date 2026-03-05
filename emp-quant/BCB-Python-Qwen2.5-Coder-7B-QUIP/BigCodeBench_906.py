
import zipfile
import os
import re
import shutil

def task_func(source_dir: str, target_dir: str, archive_name: str = 'archive.zip') -> str:
    # Create a list to hold the paths of processed files
    processed_files = []

    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if re.match(r'.*_processed$', file):
                processed_files.append(os.path.join(root, file))

    # Create the archive path
    archive_path = os.path.join(target_dir, archive_name)

    # Create the archive
    with zipfile.ZipFile(archive_path, 'w') as zipf:
        for file in processed_files:
            zipf.write(file, os.path.relpath(file, start=source_dir))

    # Return the path to the created archive
    return archive_path