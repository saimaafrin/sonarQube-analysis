import json
import random
from datetime import datetime, timedelta
USERS = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
def task_func(file_path, num_entries, seed=None):
    """
    Create a JSON file on a specific file path with random user activity data.
    The number of entries in the JSON file is determined by num_entries. The written JSON file contains a list of dictionaries, with each dictionary representing a log entry with the following keys: 'user', 'action', and 'timestamp'.

    Parameters:
    file_path (str): The file path where the JSON file should be created.
    num_entries (int): The number of entries of random data to generate.
    seed (int, optional): The seed for random data generation. Default is None.

    Returns:
    str: The file path of the generated JSON file.

    Requirements:
    - os
    - json
    - random
    - datetime

    Example:
    >>> task_func('/tmp/log.json', 100)
    '/tmp/log.json'
    """
    if seed is None:
        seed = random.randint(0, 1000000)
    random.seed(seed)
    entries = []
    for i in range(num_entries):
        user = random.choice(USERS)
        action = random.choice(['login', 'logout', 'click', 'search'])
        timestamp = datetime.now() - timedelta(seconds=random.randint(0, 1000000))
        entry = {'user': user, 'action': action, 'timestamp': timestamp}
        entries.append(entry)
    with open(file_path, 'w') as f:
        json.dump(entries, f)
    return file_path