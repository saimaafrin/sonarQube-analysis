import subprocess
import os
import json
from datetime import datetime
def task_func(script_name='backup.sh', log_file='/home/user/backup_log.json'):
    # Check if the script file exists
    if not os.path.isfile(script_name):
        raise FileNotFoundError(f"The script file {script_name} does not exist.")
    
    # Initialize the log dictionary
    log_data = {
        'start_time': '',
        'end_time': '',
        'exit_status': 0
    }
    
    # Get the start time
    log_data['start_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        # Execute the script using subprocess
        result = subprocess.run([script_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log_data['exit_status'] = result.returncode
    except subprocess.CalledProcessError as e:
        # Handle errors during script execution
        log_data['exit_status'] = e.returncode
        raise RuntimeError(f"Error executing the script: {e.stderr.decode('utf-8')}")
    except FileNotFoundError as e:
        # Handle script not found error
        raise FileNotFoundError(f"The script file {script_name} does not exist.")
    
    # Get the end time
    log_data['end_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Write the log data to a JSON file
    with open(log_file, 'w') as f:
        json.dump(log_data, f, indent=4)
    
    # Return the log data
    return log_data