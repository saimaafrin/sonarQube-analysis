
import os
from datetime import datetime

# Constants
LOG_DIR = './logs'

def task_func(metrics, filename, log_dir=LOG_DIR):
    # Create the log directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create the log file if it doesn't exist
    log_file = os.path.join(log_dir, filename)
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            f.write('')

    # Write the metrics to the log file
    with open(log_file, 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'{timestamp}: {metrics}\n')

    return True