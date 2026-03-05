
import os
from datetime import datetime
# Constants
LOG_DIR = './logs'

def task_func(metrics, filename, log_dir=LOG_DIR):
    try:
        with open(os.path.join(log_dir, filename), 'a') as f:
            f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(metrics) + '\n')
        return True
    except IOError:
        return False