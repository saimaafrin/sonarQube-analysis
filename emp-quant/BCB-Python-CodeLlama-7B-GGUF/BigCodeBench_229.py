
import json
import random
from datetime import datetime, timedelta

# Constants
USERS = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']

def task_func(file_path, num_entries, seed=None):
    # Set random seed if provided
    if seed is not None:
        random.seed(seed)

    # Generate random user activity data
    user_activity_data = []
    for _ in range(num_entries):
        user = random.choice(USERS)
        action = random.choice(['logged in', 'logged out', 'clicked', 'scrolled'])
        timestamp = datetime.now() - timedelta(minutes=random.randint(0, 60))
        user_activity_data.append({'user': user, 'action': action, 'timestamp': timestamp})

    # Write data to JSON file
    with open(file_path, 'w') as f:
        json.dump(user_activity_data, f)

    return file_path

task_func(file_path, num_entries, seed)