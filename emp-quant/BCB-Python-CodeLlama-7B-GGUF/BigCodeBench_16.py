
import os
import glob
import subprocess

def task_func(directory, backup_dir='/path/to/backup'):
    if not os.path.exists(directory):
        raise FileNotFoundError(f'Directory {directory} does not exist')

    log_files = glob.glob(os.path.join(directory, '*.log'))
    if not log_files:
        return 'No logs found to backup'

    backup_file = os.path.join(backup_dir, 'logs_backup.tar.gz')
    subprocess.run(['tar', '-czf', backup_file] + log_files)
    for log_file in log_files:
        os.remove(log_file)

    return backup_file