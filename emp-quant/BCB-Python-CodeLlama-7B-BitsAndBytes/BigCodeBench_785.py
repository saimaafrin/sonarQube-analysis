
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

    # Archive each file and delete the original
    for file in files:
        archive_file = os.path.join(ARCHIVE_DIR, file)
        subprocess.run(['tar', '-czf', archive_file, file])
        os.remove(file)

    # Return the archive file path
    return archive_file