
import subprocess
import os
import glob

# Constants
ARCHIVE_DIR = '/tmp/archive'

def task_func(pattern):
    # Create the archive directory if it doesn't exist
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    # Get a list of files that match the pattern
    files = glob.glob(pattern)

    # Archive each file
    for file in files:
        # Get the file name and extension
        file_name, file_ext = os.path.splitext(file)

        # Create the archive file path
        archive_file = os.path.join(ARCHIVE_DIR, file_name + '.tar.gz')

        # Create the tar command
        tar_cmd = ['tar', '-czf', archive_file, file]

        # Run the tar command
        subprocess.run(tar_cmd)

        # Delete the original file
        os.remove(file)

    # Return the archive file path
    return archive_file