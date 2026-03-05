import zipfile
import os
import re
import shutil
def task_func(source_dir: str, target_dir: str, archive_name: str = 'archive.zip') -> str:
    """
    Archives all processed files from a source directory to a target directory.
    The function identifies processed files by the '_processed' suffix in the filename.
    """
    # Create a list of processed files
    processed_files = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if re.search('_processed$', file):
                processed_files.append(os.path.join(root, file))

    # Create a zip archive
    archive_path = os.path.join(target_dir, archive_name)
    with zipfile.ZipFile(archive_path, 'w') as zip_file:
        for file in processed_files:
            zip_file.write(file, os.path.basename(file))

    return archive_path
source_dir = 'source_dir'
target_dir = 'target_dir'
archive_name = 'archive.zip'
processed_files = []