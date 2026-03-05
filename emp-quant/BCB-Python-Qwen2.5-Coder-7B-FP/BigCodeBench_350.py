import subprocess
import os
import shutil
from glob import glob
def task_func(src_folder, dst_folder):
    # Initialize the result dictionary
    result = {
        'success': True,
        'message': 'All files compressed and moved successfully.',
        'failed_files': []
    }

    # Ensure the destination folder exists
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    # Get a list of all files in the source folder
    files = glob(os.path.join(src_folder, '*'))

    for file in files:
        # Check if the item is a file
        if os.path.isfile(file):
            try:
                # Compress the file using gzip
                subprocess.run(['gzip', file], check=True)
                # Move the compressed file to the destination folder
                shutil.move(file + '.gz', dst_folder)
            except subprocess.CalledProcessError as e:
                # If an error occurs, update the result dictionary
                result['success'] = False
                result['message'] = f'Failed to compress or move file: {file}'
                result['failed_files'].append(file)
                # Optionally, you can re-raise the exception if you want the function to stop on error
                # raise e

    return result