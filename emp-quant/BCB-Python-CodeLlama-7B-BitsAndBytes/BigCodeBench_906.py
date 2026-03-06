
import zipfile
import os
import re
import shutil

def task_func(source_dir: str, target_dir: str, archive_name: str = 'archive.zip') -> str:
    # Create a new zip file
    zip_file = zipfile.ZipFile(os.path.join(target_dir, archive_name), 'w')

    # Iterate over the files in the source directory
    for file in os.listdir(source_dir):
        # Check if the file is processed
        if re.search('_processed$', file):
            # Add the file to the zip file
            zip_file.write(os.path.join(source_dir, file), file)

    # Close the zip file
    zip_file.close()

    # Return the path to the created archive
    return os.path.join(target_dir, archive_name)