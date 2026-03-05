import json
import random
from datetime import datetime, timedelta
USERS = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
def task_func(file_path, num_entries, seed=None):
    """
    Creates a JSON file with random user activity data.

    Args:
        file_path (str): The file path to write the JSON file to.
        num_entries (int): The number of log entries to generate.
        seed (int, optional): The random seed to use. Defaults to None.

    Returns:
        str: The file path of the generated JSON file.
    """
    if seed is not None:
        random.seed(seed)

    log_entries = []
    for _ in range(num_entries):
        user = random.choice(USERS)
        action = random.choice(['login', 'logout', 'click', 'scroll'])
        timestamp = datetime.now() - timedelta(minutes=random.randint(0, 60))
        log_entries.append({'user': user, 'action': action, 'timestamp': timestamp})

    with open(file_path, 'w') as f:
        json.dump(log_entries, f)

    return file_path