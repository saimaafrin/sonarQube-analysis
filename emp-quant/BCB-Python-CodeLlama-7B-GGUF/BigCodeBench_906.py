
import zipfile
import os
import re
import shutil

def task_func(source_dir: str, target_dir: str, archive_name: str = 'archive.zip') -> str:
    """
    Archives all processed files from a source directory to a target directory.

    :param source_dir: The source directory to archive from.
    :param target_dir: The target directory to archive to.
    :param archive_name: The name of the archive file.
    :return: The path to the created archive.
    """
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Create the archive file
    archive_path = os.path.join(target_dir, archive_name)
    with zipfile.ZipFile(archive_path, 'w') as archive:
        # Iterate over the files in the source directory
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # Check if the file is processed
                if re.search(r'_processed$', file):
                    # Add the file to the archive
                    archive.write(os.path.join(root, file))

    return archive_path