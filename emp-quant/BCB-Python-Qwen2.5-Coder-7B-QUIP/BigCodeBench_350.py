
import subprocess
import os
import shutil
from glob import glob

def task_func(src_folder, dst_folder):
    # Ensure the destination folder exists
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    # Get a list of all files in the source folder
    files = glob(os.path.join(src_folder, '*'))

    # Initialize a list to keep track of failed files
    failed_files = []

    # Iterate over the files and compress them using gzip
    for file in files:
        if os.path.isfile(file):
            try:
                # Compress the file using gzip
                subprocess.run(['gzip', file], check=True)
                # Move the compressed file to the destination folder
                shutil.move(file + '.gz', dst_folder)
            except subprocess.CalledProcessError as e:
                print(f"Failed to compress {file}: {e}")
                failed_files.append(file)

    # Check if all files were successful
    success = len(failed_files) == 0

    # Return the result as a dictionary
    return {
        'success': success,
        'message': f"{'All files were compressed and moved successfully.' if success else 'Some files failed to compress or move.'}",
        'failed_files': failed_files
    }