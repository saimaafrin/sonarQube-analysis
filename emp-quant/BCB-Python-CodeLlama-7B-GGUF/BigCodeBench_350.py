
import subprocess
import os
import shutil
from glob import glob

def task_func(src_folder, dst_folder):
    # Check if source folder exists
    if not os.path.exists(src_folder):
        return {'success': False, 'message': f'Source folder {src_folder} does not exist'}

    # Check if destination folder exists
    if not os.path.exists(dst_folder):
        return {'success': False, 'message': f'Destination folder {dst_folder} does not exist'}

    # Get list of files in source folder
    files = glob(os.path.join(src_folder, '*'))

    # Compress files using gzip
    for file in files:
        try:
            subprocess.run(['gzip', file], check=True)
        except subprocess.CalledProcessError as e:
            return {'success': False, 'message': f'Failed to compress file {file}: {e}'}

    # Move compressed files to destination folder
    for file in files:
        try:
            shutil.move(file + '.gz', dst_folder)
        except shutil.Error as e:
            return {'success': False, 'message': f'Failed to move file {file}.gz to destination folder: {e}'}

    return {'success': True, 'message': f'Successfully compressed and moved {len(files)} files'}