
import os
import glob
import subprocess
def task_func(directory, backup_dir='/path/to/backup'):
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist.")
    
    # Find all .log files in the directory
    log_files = glob.glob(os.path.join(directory, '*.log'))
    
    # If no log files are found, return a message
    if not log_files:
        return 'No logs found to backup'
    
    # Create the backup file path
    backup_file = os.path.join(backup_dir, 'logs_backup.tar.gz')
    
    # Create the tar.gz file
    subprocess.run(['tar', '-czf', backup_file, '-C', directory, '.'])
    
    # Delete the original .log files
    for log_file in log_files:
        os.remove(log_file)
    
    # Return the path to the backup file
    return backup_file