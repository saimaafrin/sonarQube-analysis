import os
from datetime import datetime
LOG_DIR = './logs'
def task_func(metrics, filename, log_dir=LOG_DIR):
    """
    Write a dictionary of metrics to a specified log file, appending a timestamp to each entry.
    """
    # Check if the log directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create a timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open the log file
    with open(os.path.join(log_dir, filename), 'a') as f:
        # Write the metrics to the file
        for key, value in metrics.items():
            f.write(f"{key}: {value} ({timestamp})\n")

    # Return True if the metrics were successfully written to the file
    return True
metrics = {'precision': 0.75, 'recall': 0.80}