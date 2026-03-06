import os
from datetime import datetime
LOG_DIR = './logs'
def task_func(metrics, filename, log_dir=LOG_DIR):
    """
    This function writes a dictionary of metrics to a specified log file, appending a timestamp to each entry.
    
    Parameters:
    - metrics (dict): A dictionary containing metric names as keys and their corresponding values.
    - filename (str): The name of the file to which the metrics will be logged.
    - log_dir (str, optional): The directory where the log file is stored. Default is './logs'.
    
    Returns:
    - bool: True if the metrics were successfully written to the file, False otherwise.
    
    Requirements:
    - os
    - datetime
    
    Examples:
    >>> metrics = {'accuracy': 0.98, 'loss': 0.05}
    >>> task_func(metrics, 'metrics.log')
    An error occurred: [Errno 2] No such file or directory: './logs/metrics.log'
    False
    
    >>> metrics = {'precision': 0.75, 'recall': 0.80}
    >>> task_func(metrics, 'evaluation.log')
    An error occurred: [Errno 2] No such file or directory: './logs/evaluation.log'
    False
    """
    try:
        # Create the log directory if it doesn't exist
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # Create the log file if it doesn't exist
        if not os.path.exists(os.path.join(log_dir, filename)):
            with open(os.path.join(log_dir, filename), 'w') as f:
                f.write('')
        
        # Write the metrics to the log file
        with open(os.path.join(log_dir, filename), 'a') as f:
            f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            for key, value in metrics.items():
                f.write(f' {key}: {value}')
            f.write('\n')
        
        return True
    except Exception as e:
        print(f'An error occurred: {e}')
        return False