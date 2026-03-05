
import subprocess
import os
import shutil
from glob import glob

def task_func(src_folder, dst_folder):
    # Check if the source and destination folders exist
    if not os.path.exists(src_folder) or not os.path.exists(dst_folder):
        return {'success': False, 'message': 'Source or destination folder does not exist', 'failed_files': []}

    # Get a list of all files in the source folder
    files = glob(src_folder + '/*')

    # Compress each file using the 'gzip' command
    for file in files:
        try:
            subprocess.run(['gzip', file])
        except subprocess.CalledProcessError:
            return {'success': False, 'message': 'Failed to compress file: ' + file, 'failed_files': [file]}

    # Move the compressed files to the destination folder
    for file in files:
        try:
            shutil.move(file, dst_folder)
        except shutil.Error:
            return {'success': False, 'message': 'Failed to move file: ' + file, 'failed_files': [file]}

    return {'success': True, 'message': 'All files compressed and moved successfully', 'failed_files': []}