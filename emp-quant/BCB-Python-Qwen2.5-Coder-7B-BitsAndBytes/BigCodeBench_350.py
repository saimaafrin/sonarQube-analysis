
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

    success = True
    failed_files = []

    for file in files:
        try:
            # Compress the file using gzip
            subprocess.run(['gzip', file], check=True)
            
            # Move the compressed file to the destination folder
            shutil.move(file + '.gz', dst_folder)
        except Exception as e:
            success = False
            failed_files.append((file, str(e)))

    return {
        'success': success,
        'message': 'All files processed.' if success else f'Some files failed.',
        'failed_files': failed_files
    }