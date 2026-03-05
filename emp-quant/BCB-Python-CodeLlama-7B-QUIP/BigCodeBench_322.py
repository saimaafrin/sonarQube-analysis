
import subprocess
import os
import shutil
import sys

# Constants
DIRECTORY = 'c:\Program Files\VMware\VMware Server'
BACKUP_DIRECTORY = 'c:\Program Files\VMware\VMware Server\Backup'

def task_func(filename):
    # Backup the file
    backup_file = os.path.join(BACKUP_DIRECTORY, filename)
    shutil.copy(os.path.join(DIRECTORY, filename), backup_file)

    # Execute the file as a subprocess
    try:
        subprocess.Popen(os.path.join(DIRECTORY, filename))
    except OSError:
        sys.stderr.write("Error executing file")
        return -1

    return 0