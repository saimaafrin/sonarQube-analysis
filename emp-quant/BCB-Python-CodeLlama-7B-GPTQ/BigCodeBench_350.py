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
    # Check if the source folder exists
    if not os.path.exists(src_folder):
        return {
            'success': False,
            'message': f"Source folder '{src_folder}' does not exist.",
            'failed_files': []
        }

    # Check if the destination folder exists
    if not os.path.exists(dst_folder):
        return {
            'success': False,
            'message': f"Destination folder '{dst_folder}' does not exist.",
            'failed_files': []
        }

    # Get a list of all files in the source folder
    files = glob(os.path.join(src_folder, '*'))

    # Compress each file using the 'gzip' command
    failed_files = []
    for file in files:
        try:
            subprocess.run(['gzip', file])
        except subprocess.CalledProcessError:
            failed_files.append(file)

    # Move the compressed files to the destination folder
    for file in files:
        try:
            shutil.move(file + '.gz', dst_folder)
        except shutil.Error:
            failed_files.append(file)

    # Return the result
    return {
        'success': len(failed_files) == 0,
        'message': f"Compressed and moved {len(files)} files.",
        'failed_files': failed_files
    }
src_folder = 'source_folder'
dst_folder = 'destination_folder'