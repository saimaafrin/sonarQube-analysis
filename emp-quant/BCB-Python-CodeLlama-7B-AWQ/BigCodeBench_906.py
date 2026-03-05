import zipfile
import os
import re
import shutil
def task_func(source_dir: str, target_dir: str, archive_name: str = 'archive.zip') -> str:
    """
    Archives all processed files from a source directory to a target directory.
    The function identifies processed files by the '_processed' suffix in the filename.
    """
    # Create a list of all files in the source directory
    files = os.listdir(source_dir)

    # Create a list of processed files
    processed_files = [file for file in files if re.search('_processed$', file)]

    # Create a list of unprocessed files
    unprocessed_files = [file for file in files if not re.search('_processed$', file)]

    # Create a zip file of the processed files
    with zipfile.ZipFile(os.path.join(target_dir, archive_name), 'w') as zip_file:
        for file in processed_files:
            zip_file.write(os.path.join(source_dir, file), os.path.join(target_dir, file))

    # Move the unprocessed files to the target directory
    for file in unprocessed_files:
        shutil.move(os.path.join(source_dir, file), os.path.join(target_dir, file))

    # Return the path to the created archive
    return os.path.join(target_dir, archive_name)
source_dir = 'source_dir'
target_dir = 'target_dir'
archive_name = 'archive.zip'
processed_files = ['file1_processed.txt', 'file2_processed.txt']
unprocessed_files = ['file1.txt', 'file2.txt']