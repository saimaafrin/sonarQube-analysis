
import zipfile
import os
import re
import shutil

def task_func(source_dir: str, target_dir: str, archive_name: str = 'archive.zip') -> str:
    """
    Archives all processed files from a source directory to a target directory.
    The function identifies processed files by the '_processed' suffix in the filename.
    """
    processed_files = [file for file in os.listdir(source_dir) if re.match(r'.*_processed', file)]
    archive_path = os.path.join(target_dir, archive_name)
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zip:
        for file in processed_files:
            zip.write(os.path.join(source_dir, file))
    return archive_path