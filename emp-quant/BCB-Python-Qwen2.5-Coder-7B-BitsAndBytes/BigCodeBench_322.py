
import subprocess
import os
import shutil
import sys

# Constants
DIRECTORY = 'c:\\Program Files\\VMware\\VMware Server'
BACKUP_DIRECTORY = 'c:\\Program Files\\VMware\\VMware Server\\Backup'

def task_func(filename):
    # Ensure the backup directory exists
    if not os.path.exists(BACKUP_DIRECTORY):
        try:
            os.makedirs(BACKUP_DIRECTORY)
        except Exception as e:
            print(f"Failed to create backup directory: {e}")
            return -1
    
    # Construct full file path
    full_path = os.path.join(DIRECTORY, filename)
    
    # Check if the file exists
    if not os.path.isfile(full_path):
        print(f"The file {filename} does not exist in the specified directory.")
        return -1
    
    # Backup the file
    backup_path = os.path.join(BACKUP_DIRECTORY, filename)
    try:
        shutil.copy2(full_path, backup_path)
    except Exception as e:
        print(f"Failed to backup the file: {e}")
        return -1
    
    # Execute the file as a subprocess
    try:
        result = subprocess.run([full_path], check=True, capture_output=True, text=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Subprocess failed with return code {e.returncode}. Error: {e.stderr}")
        return e.returncode
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return -1

    filename = sys.argv[1]
    exit_code = task_func(filename)
    print(f"Exit Code: {exit_code}")