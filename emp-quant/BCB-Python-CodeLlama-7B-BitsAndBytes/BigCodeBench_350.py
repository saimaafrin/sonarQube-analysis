
import subprocess
import os
import shutil
from glob import glob

def task_func(src_folder, dst_folder):
    # Create a dictionary to store the results
    results = {'success': True, 'message': '', 'failed_files': []}

    # Get a list of all files in the source folder
    files = glob(os.path.join(src_folder, '*'))

    # Compress each file using gzip
    for file in files:
        try:
            # Compress the file using gzip
            subprocess.run(['gzip', file])

            # Move the compressed file to the destination folder
            shutil.move(file + '.gz', dst_folder)
        except Exception as e:
            # If an error occurs, set the success flag to False and add the file to the failed_files list
            results['success'] = False
            results['message'] = 'Error compressing and moving files'
            results['failed_files'].append(file)
            break

    return results