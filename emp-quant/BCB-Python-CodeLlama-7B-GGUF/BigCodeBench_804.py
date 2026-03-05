
import os
from datetime import datetime
# Constants
LOG_DIR = './logs'
def task_func(metrics, filename, log_dir=LOG_DIR):
    # Check if the log directory exists
    if not os.path.exists(log_dir):
        print(f"Log directory {log_dir} does not exist.")
        return False

    # Create the log file if it does not exist
    log_file = os.path.join(log_dir, filename)
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            f.write('')

    # Write the metrics to the log file
    with open(log_file, 'a') as f:
        f.write(f"{datetime.now()} - {metrics}\n")

    return True