import subprocess
import os
import json
from datetime import datetime
def task_func(script_name='backup.sh', log_file='/home/user/backup_log.json'):
    """
    Runs the provided backup shell script and logs the start time, end time, and exit status in a specified JSON log file.
    The function should raise the exception for:
        FileNotFoundError: If the script file does not exist.
        RuntimeError: If there is an error executing the script.
    The function should output with:
        dict: A dictionary containing:
            'start_time': The start time of the script execution in the format '%Y-%m-%d %H:%M:%S'.
            'end_time': The end time of the script execution in the format '%Y-%m-%d %H:%M:%S'.
            'exit_status': The exit status of the script execution (0 for success, other values indicate an error).
    """
    # Check if the script file exists
    if not os.path.isfile(script_name):
        raise FileNotFoundError(f"Script file '{script_name}' does not exist.")

    # Log the start time
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_data = {'start_time': start_time}

    # Run the script
    try:
        subprocess.run(script_name, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error executing script: {e}")

    # Log the end time and exit status
    end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_data['end_time'] = end_time
    log_data['exit_status'] = e.returncode

    # Write the log data to the log file
    with open(log_file, 'w') as f:
        json.dump(log_data, f)

    return log_data
script_name = 'backup.sh'
log_file = '/home/user/backup_log.json'