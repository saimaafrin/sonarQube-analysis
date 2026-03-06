
import zipfile
import os
import re
import shutil

def task_func(source_dir: str, target_dir: str, archive_name: str = 'archive.zip') -> str:
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Create a list of processed files
    processed_files = [f for f in os.listdir(source_dir) if re.search(r'_processed$', f)]

    # If no processed files, return None
    if not processed_files:
        return None

    # Create the full path for the archive
    archive_path = os.path.join(target_dir, archive_name)

    # Create a zip file and add the processed files to it
    with zipfile.ZipFile(archive_path, 'w') as zipf:
        for file in processed_files:
            file_path = os.path.join(source_dir, file)
            zipf.write(file_path, arcname=file)

    # Move the archive to the target directory
    shutil.move(archive_path, target_dir)

    # Return the path to the created archive
    return os.path.join(target_dir, archive_name)