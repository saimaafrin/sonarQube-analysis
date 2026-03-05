
import json
import random
from datetime import datetime, timedelta
# Constants
USERS = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
def task_func(file_path, num_entries, seed=None):
    # Set random seed if provided
    if seed:
        random.seed(seed)
    # Generate random user activity data
    user_activity = []
    for i in range(num_entries):
        user_activity.append({
            'user': random.choice(USERS),
            'action': random.choice(['login', 'logout', 'click', 'scroll']),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    # Write data to JSON file
    with open(file_path, 'w') as f:
        json.dump(user_activity, f)
    return file_path