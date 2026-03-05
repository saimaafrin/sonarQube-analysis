
import pandas as pd
from datetime import datetime, timedelta
import random

def task_func(epoch_milliseconds, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)

    # Convert the start time from milliseconds to seconds
    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000.0)

    # Get the current time
    current_time = datetime.now()

    # Check if the start time is after the current time
    if start_time > current_time:
        raise ValueError("Start time is after the current system time.")

    # Define the list of users and activities
    users = ['user1', 'user2', 'user3', 'user4', 'user5']
    activities = ['login', 'logout', 'browse', 'search', 'purchase']

    # Initialize the list to store the log entries
    log_entries = []

    # Iterate from the start time to the current time
    current_time = start_time
    while current_time <= current_time:
        # Generate a random number of seconds between 1 and 10
        random_seconds = random.randint(1, 10)

        # Add the current time to the log entries
        log_entries.append({
            'User': random.choice(users),
            'Activity': random.choice(activities),
            'Time': current_time
        })

        # Increment the current time by the random number of seconds
        current_time += timedelta(seconds=random_seconds)

    # Convert the log entries to a DataFrame
    log_df = pd.DataFrame(log_entries)

    return log_df