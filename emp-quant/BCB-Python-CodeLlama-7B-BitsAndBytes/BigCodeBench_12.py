
import subprocess
import os
import json
from datetime import datetime

def task_func(script_name='backup.sh', log_file='/home/user/backup_log.json'):
    # Check if the script file exists
    if not os.path.isfile(script_name):
        raise FileNotFoundError(f"Script file {script_name} does not exist")

    # Start the script execution
    start_time = datetime.now()
    process = subprocess.Popen(script_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    exit_status = process.returncode

    # Log the start and end times and exit status
    log_data = {
        'start_time': start_time.strftime('%Y-%m-%d %H:%M:%S'),
        'end_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'exit_status': exit_status
    }
    with open(log_file, 'w') as f:
        json.dump(log_data, f)

    # Return the log data
    return log_data