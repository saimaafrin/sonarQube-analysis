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

    # Set the random seed
    random.seed(seed)

    # Initialize the DataFrame
    df = pd.DataFrame(columns=['User', 'Activity', 'Time'])

    # Iterate from the starting epoch time to the current system time
    current_time = datetime.fromtimestamp(epoch_milliseconds / 1000)
    while current_time <= datetime.now():
        # Increment the time by a random number of seconds
        new_time = current_time + timedelta(seconds=random.randint(1, 10))

        # Choose a random user and activity
        user = random.choice(['user1', 'user2', 'user3', 'user4', 'user5'])
        activity = random.choice(['login', 'logout', 'browse', 'search', 'purchase'])

        # Add the log entry to the DataFrame
        df = df.append({'User': user, 'Activity': activity, 'Time': new_time}, ignore_index=True)

        # Update the current time
        current_time = new_time

    return df