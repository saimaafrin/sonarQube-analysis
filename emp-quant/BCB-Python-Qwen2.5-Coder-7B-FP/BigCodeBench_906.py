import zipfile
import os
import re
import shutil
def task_func(source_dir: str, target_dir: str, archive_name: str = 'archive.zip') -> str:
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Create a list to hold the paths of processed files
    processed_files = []

    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check if the file has the '_processed' suffix
            if re.search(r'_processed$', file):
                # Construct the full path to the file
                file_path = os.path.join(root, file)
                # Add the file path to the list
                processed_files.append(file_path)

    # Create a zip file in the target directory
    archive_path = os.path.join(target_dir, archive_name)
    with zipfile.ZipFile(archive_path, 'w') as zipf:
        # Add each processed file to the zip archive
        for file_path in processed_files:
            # Calculate the arcname (relative path) for the zip file
            arcname = os.path.relpath(file_path, start=source_dir)
            # Add the file to the zip archive
            zipf.write(file_path, arcname)

    # Return the path to the created archive
    return archive_path