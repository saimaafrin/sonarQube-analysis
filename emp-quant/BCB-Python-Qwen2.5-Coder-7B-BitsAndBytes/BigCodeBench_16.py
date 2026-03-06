
import os
import glob
import subprocess

def task_func(directory, backup_dir='/path/to/backup'):
    # Check if the specified directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    
    # Find all .log files in the specified directory
    log_files = glob.glob(os.path.join(directory, '*.log'))
    
    # If no log files are found, return a message
    if not log_files:
        return 'No logs found to backup'
    
    # Create the backup directory if it doesn't exist
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # Define the path for the backup file
    backup_file_path = os.path.join(backup_dir, 'logs_backup.tar.gz')
    
    # Use tar command to create a compressed archive of the log files
    subprocess.run(['tar', '-czf', backup_file_path] + log_files)
    
    # Delete the original log files
    for log_file in log_files:
        os.remove(log_file)
    
    # Return the path to the backup file
    return backup_file_path