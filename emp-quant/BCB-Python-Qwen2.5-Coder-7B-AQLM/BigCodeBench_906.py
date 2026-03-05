
import zipfile
import os
import re
import shutil

def task_func(source_dir: str, target_dir: str, archive_name: str = 'archive.zip') -> str:
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Create the archive path
    archive_path = os.path.join(target_dir, archive_name)

    # Create a zip file
    with zipfile.ZipFile(archive_path, 'w') as zipf:
        # Walk through the source directory
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # Check if the file has the '_processed' suffix
                if re.search(r'_processed$', file):
                    # Create the full file path
                    file_path = os.path.join(root, file)
                    # Add the file to the zip archive
                    zipf.write(file_path, os.path.relpath(file_path, source_dir))

    return archive_path