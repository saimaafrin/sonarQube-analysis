
import subprocess
import os
import glob
# Constants
ARCHIVE_DIR = '/tmp/archive'

def task_func(pattern):
    # Create the archive directory if it doesn't exist
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    # Find all files matching the pattern
    files_to_archive = glob.glob(pattern)

    # Create an archive file
    archive_file = os.path.join(ARCHIVE_DIR, 'archive.tar.gz')
    with subprocess.Popen(['tar', '-czf', archive_file] + files_to_archive, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise Exception(f"Error creating archive: {stderr.decode()}")

    # Delete the original files
    for file in files_to_archive:
        os.remove(file)

    return archive_file