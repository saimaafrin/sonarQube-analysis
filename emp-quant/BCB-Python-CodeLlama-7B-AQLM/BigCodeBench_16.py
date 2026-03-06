import os
import glob
import subprocess
def task_func(directory, backup_dir='/path/to/backup'):
    """
    Backup all '.log' files in a specified directory to a tar.gz file and delete the original files after backup.
    The backup file is named 'logs_backup.tar.gz' and placed in the specified backup directory.
    
    Parameters:
    - directory (str): The directory that contains the log files to be backed up.
    - backup_dir (str, optional): The directory where the backup file will be saved.
                                  Default is '/path/to/backup'.
    
    Returns:
    - str: The path to the backup file if logs are found, otherwise returns a message 'No logs found to backup'.
    
    Raises:
    - FileNotFoundError: If the specified directory does not exist.
    
    Requirements:
    - subprocess
    - glob
    - os
    
    Example:
    >>> task_func('/path/to/logs')
    '/path/to/backup/logs_backup.tar.gz'
    >>> task_func('/path/to/logs', '/alternative/backup/dir')
    '/alternative/backup/dir/logs_backup.tar.gz'
    """
    if not os.path.exists(directory):
        raise FileNotFoundError('The specified directory does not exist.')
    if not os.path.exists(backup_dir):
        os.mkdir(backup_dir)
    log_files = glob.glob(directory + '/*.log')
    if len(log_files) == 0:
        return 'No logs found to backup.'
    else:
        subprocess.call(['tar', '-czf', backup_dir + '/logs_backup.tar.gz'] + log_files)
        for log_file in log_files:
            os.remove(log_file)
        return backup_dir + '/logs_backup.tar.gz'