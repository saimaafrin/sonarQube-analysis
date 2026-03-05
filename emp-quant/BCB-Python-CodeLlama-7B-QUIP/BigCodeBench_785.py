
import subprocess
import os
import glob
# Constants
ARCHIVE_DIR = '/tmp/archive'
def task_func(pattern):
    # Get the list of files that match the pattern
    files = glob.glob(pattern)
    # Iterate over the files and archive them
    for file in files:
        # Create the archive file name
        archive_file = os.path.join(ARCHIVE_DIR, file + '.zip')
        # Archive the file
        subprocess.run(['zip', '-r', archive_file, file])
        # Delete the original file
        os.remove(file)
    # Return the archive file path
    return archive_file