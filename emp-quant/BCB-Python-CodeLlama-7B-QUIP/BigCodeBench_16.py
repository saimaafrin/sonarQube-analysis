
import os
import glob
import subprocess

def task_func(directory, backup_dir='/path/to/backup'):
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist")
    files = glob.glob(os.path.join(directory, '*.log'))
    if not files:
        return "No logs found to backup"
    with open(os.path.join(backup_dir, 'logs_backup.tar.gz'), 'wb') as f:
        for file in files:
            with open(file, 'rb') as f_in:
                f.write(f_in.read())
    for file in files:
        os.remove(file)
    return os.path.join(backup_dir, 'logs_backup.tar.gz')