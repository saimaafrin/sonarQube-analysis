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
    try:
        # Check if the script file exists
        if not os.path.isfile(script_name):
            raise FileNotFoundError(f"Script file '{script_name}' does not exist")

        # Log the start time
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a") as f:
            f.write(f"{start_time}\n")

        # Run the script
        process = subprocess.run(script_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Log the end time
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a") as f:
            f.write(f"{end_time}\n")

        # Log the exit status
        exit_status = process.returncode
        with open(log_file, "a") as f:
            f.write(f"{exit_status}\n")

        # Return the dictionary with the start time, end time, and exit status
        return {
            "start_time": start_time,
            "end_time": end_time,
            "exit_status": exit_status
        }

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except RuntimeError as e:
        print(f"Error: {e}")