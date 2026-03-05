import subprocess
import os
import json
from datetime import datetime
def task_func(script_name='backup.sh', log_file='/home/user/backup_log.json'):
    # Check if the script file exists
    if not os.path.isfile(script_name):
        raise FileNotFoundError(f"The script file {script_name} does not exist.")
    
    # Get the start time
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Execute the script
    try:
        result = subprocess.run(['bash', script_name], check=True, capture_output=True, text=True)
        exit_status = result.returncode
    except subprocess.CalledProcessError as e:
        exit_status = e.returncode
        raise RuntimeError(f"Error executing the script: {e.stderr}")
    
    # Get the end time
    end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Prepare the log data
    log_data = {
        'start_time': start_time,
        'end_time': end_time,
        'exit_status': exit_status
    }
    
    # Write the log data to the specified JSON file
    with open(log_file, 'w') as f:
        json.dump(log_data, f, indent=4)
    
    return log_data