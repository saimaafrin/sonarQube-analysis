
import pandas as pd
from datetime import datetime, timedelta
import random

def task_func(epoch_milliseconds, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)

    # Define the list of users and activities
    users = ['user1', 'user2', 'user3', 'user4', 'user5']
    activities = ['login', 'logout', 'browse', 'search', 'purchase']

    # Initialize the DataFrame to store the logs
    logs = pd.DataFrame(columns=['User', 'Activity', 'Time'])

    # Iterate from the starting epoch time to the current time, incrementing by a random number of seconds between each log entry
    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000)
    current_time = datetime.now()
    while start_time <= current_time:
        # Generate a random user and activity
        user = random.choice(users)
        activity = random.choice(activities)

        # Generate a random time between the start time and the current time
        time = start_time + timedelta(seconds=random.randint(1, 10))

        # Add the log entry to the DataFrame
        logs = logs.append({'User': user, 'Activity': activity, 'Time': time}, ignore_index=True)

        # Increment the start time by the random number of seconds
        start_time += timedelta(seconds=random.randint(1, 10))

    # Return the DataFrame containing the logs
    return logs