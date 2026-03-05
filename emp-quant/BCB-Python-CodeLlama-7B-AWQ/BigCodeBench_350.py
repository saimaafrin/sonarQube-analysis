import subprocess
import os
import shutil
from glob import glob
def task_func(src_folder, dst_folder):
    """
    Compress all files in the specified source folder and move the compressed files to a destination folder.
    This operation is executed as a background process using the 'gzip' command.
    The function should output with:
        dict: A dictionary containing:
            'success': A boolean indicating if all files were compressed and moved successfully.
            'message': A descriptive message about the operation's result.
            'failed_files': A list of filenames that failed to compress or move.
    """
    # Check if source folder exists
    if not os.path.exists(src_folder):
        return {'success': False, 'message': f'Source folder {src_folder} does not exist.', 'failed_files': []}

    # Check if destination folder exists
    if not os.path.exists(dst_folder):
        return {'success': False, 'message': f'Destination folder {dst_folder} does not exist.', 'failed_files': []}

    # Get list of files in source folder
    files = glob(os.path.join(src_folder, '*'))

    # Compress files
    for file in files:
        try:
            subprocess.run(['gzip', file], check=True)
        except subprocess.CalledProcessError as e:
            return {'success': False, 'message': f'Failed to compress file {file}.', 'failed_files': [file]}

    # Move compressed files to destination folder
    for file in files:
        try:
            shutil.move(file + '.gz', dst_folder)
        except shutil.Error as e:
            return {'success': False, 'message': f'Failed to move file {file}.', 'failed_files': [file]}

    return {'success': True, 'message': f'All files compressed and moved successfully.', 'failed_files': []}
src_folder = 'src'
dst_folder = 'dst'