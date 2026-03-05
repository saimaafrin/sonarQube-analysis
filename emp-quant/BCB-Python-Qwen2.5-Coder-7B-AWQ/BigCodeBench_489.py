import pandas as pd
from datetime import datetime, timedelta
import random
def task_func(epoch_milliseconds, seed=0):
    # Set the seed for random number generation
    random.seed(seed)
    
    # Convert epoch time to datetime
    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000)
    current_time = datetime.now()
    
    # Check if start time is after the current system time
    if start_time > current_time:
        raise ValueError("Start time is after the current system time.")
    
    # Define lists of users and activities
    users = ['user1', 'user2', 'user3', 'user4', 'user5']
    activities = ['login', 'logout', 'browse', 'search', 'purchase']
    
    # Initialize an empty list to store log entries
    logs = []
    
    # Generate user activity logs
    current_log_time = start_time
    while current_log_time < current_time:
        # Randomly select a user and an activity
        user = random.choice(users)
        activity = random.choice(activities)
        
        # Append the log entry to the list
        logs.append({'User': user, 'Activity': activity, 'Time': current_log_time})
        
        # Increment the time by a random number of seconds between 1 and 10
        increment_seconds = random.randint(1, 10)
        current_log_time += timedelta(seconds=increment_seconds)
    
    # Convert the list of logs to a DataFrame
    df = pd.DataFrame(logs)
    
    return df