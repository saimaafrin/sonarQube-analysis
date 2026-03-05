
import subprocess
import os
import glob
# Constants
ARCHIVE_DIR = '/tmp/archive'

def task_func(pattern):
    # Ensure the archive directory exists
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    # Find all files matching the pattern
    files_to_archive = glob.glob(pattern)

    # Create an archive file
    archive_file = os.path.join(ARCHIVE_DIR, 'archive.tar.gz')
    subprocess.run(['tar', '-czf', archive_file, '-i', '-'], input='\n'.join(files_to_archive), text=True)

    # Delete the original files
    for file_to_archive in files_to_archive:
        os.remove(file_to_archive)

    return archive_file