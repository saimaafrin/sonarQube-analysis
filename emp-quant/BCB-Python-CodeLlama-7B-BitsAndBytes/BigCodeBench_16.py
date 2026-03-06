
import os
import glob
import subprocess

def task_func(directory, backup_dir='/path/to/backup'):
    # Check if the specified directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist")

    # Get a list of all '.log' files in the specified directory
    log_files = glob.glob(os.path.join(directory, '*.log'))

    # If no logs are found, return a message
    if not log_files:
        return "No logs found to backup"

    # Create a tar file with the backup name
    tar_file = os.path.join(backup_dir, 'logs_backup.tar.gz')

    # Compress the log files into the tar file
    subprocess.run(['tar', '-czf', tar_file] + log_files)

    # Delete the original log files
    for log_file in log_files:
        os.remove(log_file)

    # Return the path to the backup file
    return tar_file