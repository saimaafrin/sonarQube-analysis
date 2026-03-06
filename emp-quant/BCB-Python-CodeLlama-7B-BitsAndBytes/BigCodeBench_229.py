
import json
import random
from datetime import datetime, timedelta

# Constants
USERS = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']

def task_func(file_path, num_entries, seed=None):
    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)

    # Create a list of dictionaries to store the log entries
    log_entries = []

    # Generate random user activity data
    for i in range(num_entries):
        user = random.choice(USERS)
        action = random.choice(['opened', 'closed', 'deleted'])
        timestamp = datetime.now() - timedelta(minutes=random.randint(0, 60))

        log_entries.append({
            'user': user,
            'action': action,
            'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S')
        })

    # Write the log entries to a JSON file
    with open(file_path, 'w') as f:
        json.dump(log_entries, f)

    return file_path

task_func(file_path, num_entries, seed)