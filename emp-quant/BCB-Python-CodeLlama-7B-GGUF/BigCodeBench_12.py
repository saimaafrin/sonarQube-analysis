
import subprocess
import os
import json
from datetime import datetime

def task_func(script_name='backup.sh', log_file='/home/user/backup_log.json'):
    try:
        # Run the backup script
        subprocess.run(script_name, shell=True)

        # Get the start and end times of the script execution
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Get the exit status of the script execution
        exit_status = subprocess.run(script_name, shell=True).returncode

        # Create a dictionary to store the log data
        log_data = {
            'start_time': start_time,
            'end_time': end_time,
            'exit_status': exit_status
        }

        # Write the log data to the JSON log file
        with open(log_file, 'w') as f:
            json.dump(log_data, f)

        return log_data

    except FileNotFoundError:
        raise FileNotFoundError(f'Script file {script_name} does not exist')

    except RuntimeError:
        raise RuntimeError(f'Error executing script {script_name}')