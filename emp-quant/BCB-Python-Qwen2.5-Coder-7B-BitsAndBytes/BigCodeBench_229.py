
import json
import random
from datetime import datetime, timedelta

# Constants
USERS = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']

def task_func(file_path, num_entries, seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Generate random user activity data
    log_data = []
    for _ in range(num_entries):
        user = random.choice(USERS)
        action = random.choice(['login', 'logout', 'upload', 'download'])
        timestamp = datetime.now() - timedelta(days=random.randint(0, 365))
        log_entry = {
            'user': user,
            'action': action,
            'timestamp': timestamp.isoformat()
        }
        log_data.append(log_entry)
    
    # Write the log data to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(log_data, json_file, indent=4)
    
    return file_path