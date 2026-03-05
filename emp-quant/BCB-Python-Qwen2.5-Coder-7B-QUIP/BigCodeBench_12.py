
import subprocess
import os
import json
from datetime import datetime

def task_func(script_name='backup.sh', log_file='/home/user/backup_log.json'):
    # Check if the script file exists
    if not os.path.exists(script_name):
        raise FileNotFoundError(f"Script file {script_name} not found.")

    # Get the start time
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Run the script and capture the output and exit status
    try:
        result = subprocess.run(['bash', script_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        exit_status = result.returncode
        output = result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        exit_status = e.returncode
        output = e.stderr.decode('utf-8')

    # Get the end time
    end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log the results in the specified JSON log file
    with open(log_file, 'a') as f:
        json.dump({
            'start_time': start_time,
            'end_time': end_time,
            'exit_status': exit_status,
            'output': output
        }, f, indent=4)

    # Return the results as a dictionary
    return {
        'start_time': start_time,
        'end_time': end_time,
        'exit_status': exit_status
    }