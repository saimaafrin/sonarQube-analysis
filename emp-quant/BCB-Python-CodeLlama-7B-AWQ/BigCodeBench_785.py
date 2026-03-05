import subprocess
import os
import glob
ARCHIVE_DIR = '/tmp/archive'
def task_func(pattern):
    # Create the archive directory if it does not exist
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)
    # Get a list of files that match the pattern
    files = glob.glob(pattern)
    # Create a list of archive file names
    archive_files = [os.path.join(ARCHIVE_DIR, os.path.basename(f) + '.tar.gz') for f in files]
    # Create a list of commands to archive and delete the files
    commands = ['tar -czf {} {}'.format(archive_file, f) for archive_file, f in zip(archive_files, files)]
    commands.extend(['rm {}'.format(f) for f in files])
    # Run the commands
    for command in commands:
        subprocess.run(command, shell=True)
    # Return the archive file path
    return archive_files[0]