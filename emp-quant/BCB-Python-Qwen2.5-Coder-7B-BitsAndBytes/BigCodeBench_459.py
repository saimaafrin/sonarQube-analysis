
import subprocess
import os
import time
from datetime import datetime

def task_func(script_dir, scripts, delay):
    if delay < 0:
        raise ValueError("Delay cannot be negative")
    if not scripts:
        raise ValueError("No scripts provided")

    timestamps = []
    for script in scripts:
        script_path = os.path.join(script_dir, script)
        if not os.path.isfile(script_path) or not script_path.endswith('.sh'):
            print(f"Skipping non-existent or non-bash script: {script}")
            continue
        
        start_time = datetime.now()
        timestamps.append(start_time)
        
        # Execute the script using subprocess
        result = subprocess.run(['bash', script_path], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Script {script} failed with return code {result.returncode}")
            print(result.stderr)
        else:
            print(f"Script {script} executed successfully")
            print(result.stdout)
        
        # Wait for the specified delay before executing the next script
        time.sleep(delay)

    return timestamps