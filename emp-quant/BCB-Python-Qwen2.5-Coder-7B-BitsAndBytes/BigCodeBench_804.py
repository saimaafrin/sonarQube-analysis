
import os
from datetime import datetime

# Constants
LOG_DIR = './logs'

def task_func(metrics, filename, log_dir=LOG_DIR):
    # Ensure the log directory exists
    if not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir)
        except OSError as e:
            print(f"Error creating log directory {log_dir}: {e}")
            return False
    
    # Create the full path for the log file
    log_file_path = os.path.join(log_dir, filename)
    
    # Open the log file in append mode
    try:
        with open(log_file_path, 'a') as log_file:
            # Get current timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Format the metrics with the timestamp
            log_entry = f"{timestamp}: {metrics}\n"
            
            # Write the log entry to the file
            log_file.write(log_entry)
        
        return True
    except IOError as e:
        print(f"Error writing to log file {log_file_path}: {e}")
        return False