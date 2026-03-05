
import subprocess
import os
import shutil
from glob import glob

def task_func(src_folder, dst_folder):
    # Ensure the destination folder exists
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    # List all files in the source folder
    files = glob(os.path.join(src_folder, '*'))

    # Dictionary to store the result
    result = {
        'success': True,
        'message': 'All files compressed and moved successfully.',
        'failed_files': []
    }

    # Iterate over each file in the source folder
    for file in files:
        # Check if it's a file and not a directory
        if os.path.isfile(file):
            try:
                # Compress the file using gzip
                subprocess.run(['gzip', file], check=True)
                # Move the compressed file to the destination folder
                shutil.move(file + '.gz', dst_folder)
            except subprocess.CalledProcessError as e:
                # If an error occurs, add the file to the failed list
                result['success'] = False
                result['message'] = f'Failed to compress and move {file}. Error: {e}'
                result['failed_files'].append(file)

    return result