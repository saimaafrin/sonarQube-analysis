import os
import glob
import subprocess
def task_func(directory, backup_dir='/path/to/backup'):
    """
    Backup all '.log' files in a specified directory to a tar.gz file and delete the original files after backup.
    The backup file is named 'logs_backup.tar.gz' and placed in the specified backup directory.
    The function should raise the exception for:
        FileNotFoundError: If the specified directory does not exist.
    The function should output with:
        str: The path to the backup file if logs are found, otherwise returns a message 'No logs found to backup'.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist")

    # Create the backup directory if it does not exist
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Find all '.log' files in the specified directory
    log_files = glob.glob(os.path.join(directory, '*.log'))

    # Check if any '.log' files were found
    if not log_files:
        return "No logs found to backup"

    # Create the backup file
    backup_file = os.path.join(backup_dir, 'logs_backup.tar.gz')
    with tarfile.open(backup_file, 'w:gz') as tar:
        for log_file in log_files:
            tar.add(log_file, arcname=os.path.basename(log_file))

    # Delete the original files
    for log_file in log_files:
        os.remove(log_file)

    return backup_file
directory = '/path/to/logs'
backup_dir = '/path/to/backup'