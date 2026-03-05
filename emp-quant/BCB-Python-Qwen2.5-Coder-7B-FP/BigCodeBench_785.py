import subprocess
import os
import glob
ARCHIVE_DIR = '/tmp/archive'
def task_func(pattern):
    # Create the archive directory if it doesn't exist
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    # Find all files matching the pattern
    files_to_archive = glob.glob(pattern)

    if not files_to_archive:
        return None  # No files found matching the pattern

    # Create an archive file name
    archive_file = os.path.join(ARCHIVE_DIR, f'archive_{os.path.basename(pattern)}.tar.gz')

    # Archive the files
    subprocess.run(['tar', '-czf', archive_file] + files_to_archive)

    # Delete the original files
    for file in files_to_archive:
        os.remove(file)

    return archive_file