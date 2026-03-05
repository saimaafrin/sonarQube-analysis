import subprocess
import os
import glob
ARCHIVE_DIR = '/tmp/archive'
def task_func(pattern):
    # Create the archive directory if it doesn't exist
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    # Get a list of files that match the pattern
    files = glob.glob(pattern)

    # Create a new archive file
    archive_file = os.path.join(ARCHIVE_DIR, 'archive.zip')
    with zipfile.ZipFile(archive_file, 'w') as zip:
        for file in files:
            zip.write(file)

    # Delete the original files
    for file in files:
        os.remove(file)

    return archive_file
pattern = '*.txt'