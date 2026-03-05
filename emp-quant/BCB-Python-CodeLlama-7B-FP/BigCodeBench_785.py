import subprocess
import os
import glob
ARCHIVE_DIR = '/tmp/archive'
def task_func(pattern):
    """
    Archive all files that match a particular pattern and then delete the original files.
    """
    # Create the archive directory if it does not exist
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    # Get a list of files that match the pattern
    files = glob.glob(pattern)

    # Archive each file
    for file in files:
        # Get the file name and extension
        name, ext = os.path.splitext(file)

        # Create the archive file name
        archive_file = os.path.join(ARCHIVE_DIR, name + '_' + ext)

        # Archive the file
        subprocess.run(['tar', '-czf', archive_file, file])

        # Delete the original file
        os.remove(file)

    # Return the archive file path
    return archive_file
pattern = '*.txt'