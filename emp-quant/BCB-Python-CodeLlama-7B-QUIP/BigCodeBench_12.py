
import subprocess
import os
import json
from datetime import datetime

def task_func(script_name='backup.sh', log_file='/home/user/backup_log.json'):
    try:
        # Run the backup script
        process = subprocess.Popen(script_name, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Log the start and end times and exit status
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        exit_status = process.returncode

        # Write the log to the JSON file
        with open(log_file, 'w') as f:
            json.dump({
                'start_time': start_time,
                'end_time': end_time,
                'exit_status': exit_status
            }, f)
    except FileNotFoundError:
        raise Exception('Script file not found')
    except RuntimeError:
        raise Exception('Error executing script')