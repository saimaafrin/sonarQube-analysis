
import os
from datetime import datetime

# Constants
LOG_DIR = './logs'

def task_func(metrics, filename, log_dir=LOG_DIR):
    # Ensure the log directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Create the full file path
    file_path = os.path.join(log_dir, filename)
    
    try:
        # Open the file in append mode
        with open(file_path, 'a') as file:
            # Get the current timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Format the metrics with the timestamp
            log_entry = f"{timestamp} - {metrics}\n"
            # Write the log entry to the file
            file.write(log_entry)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False