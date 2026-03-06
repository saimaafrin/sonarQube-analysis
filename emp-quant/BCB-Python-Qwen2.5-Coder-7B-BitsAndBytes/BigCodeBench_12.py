
import subprocess
import os
import json
from datetime import datetime

def task_func(script_name='backup.sh', log_file='/home/user/backup_log.json'):
    try:
        # Check if the script file exists
        if not os.path.isfile(script_name):
            raise FileNotFoundError(f"The script {script_name} does not exist.")
        
        # Get the start time
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Execute the script
        result = subprocess.run(['bash', script_name], capture_output=True, text=True)
        
        # Get the end time
        end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Prepare the log data
        log_data = {
            'start_time': start_time,
            'end_time': end_time,
            'exit_status': result.returncode
        }
        
        # Write the log to the specified file
        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=4)
        
        return log_data
    
    except Exception as e:
        raise RuntimeError(f"An error occurred while running the script: {e}")