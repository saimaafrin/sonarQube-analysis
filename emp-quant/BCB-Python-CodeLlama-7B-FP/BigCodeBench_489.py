import pandas as pd
from datetime import datetime, timedelta
import random
def task_func(epoch_milliseconds, seed=0):
    """
    Generate user activity logs from a given epoch time to the current time.
    This function iterates from the starting epoch time to the current system time,
    incrementally increasing the time by a random number of seconds (an integer in [1, 10])
    between each log entry. Each log entry records a user performing an activity at a
    specific time.
    The function should raise the exception for: ValueError: If the start time is after the current system time.
    The function should output with:
        pd.DataFrame: A DataFrame containing logs of user activities, with columns:
        'User':   User names, randomly chosen from a predefined list of users,
        ['user1', 'user2', 'user3', 'user4', 'user5'].
        'Activity': Activities performed by the users, randomly chosen from a
        predefined list of activities, ['login', 'logout', 'browse',
        'search', 'purchase'].
        'Time': The timestamp of when the activity occurred, incrementally
        increasing from the starting epoch time to the current time.
    """
    # Check if the start time is after the current system time
    if epoch_milliseconds > datetime.now().timestamp() * 1000:
        raise ValueError("Start time is after the current system time")

    # Initialize the DataFrame to store the logs
    logs = pd.DataFrame(columns=['User', 'Activity', 'Time'])

    # Iterate from the starting epoch time to the current system time
    current_time = datetime.fromtimestamp(epoch_milliseconds / 1000)
    while current_time <= datetime.now():
        # Generate a random number of seconds between 1 and 10
        random_seconds = random.randint(1, 10)

        # Increment the current time by the random number of seconds
        current_time += timedelta(seconds=random_seconds)

        # Generate a random user and activity
        user = random.choice(['user1', 'user2', 'user3', 'user4', 'user5'])
        activity = random.choice(['login', 'logout', 'browse', 'search', 'purchase'])

        # Add the log entry to the DataFrame
        logs = logs.append({'User': user, 'Activity': activity, 'Time': current_time}, ignore_index=True)

    # Return the DataFrame with the logs
    return logs