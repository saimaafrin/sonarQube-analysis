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
    
    # Predefined lists of users and activities
    users = ['user1', 'user2', 'user3', 'user4', 'user5']
    activities = ['login', 'logout', 'browse', 'search', 'purchase']
    
    # Initialize an empty list to store log entries
    logs = []
    
    # Start from the start time and incrementally increase the time
    current_time = start_time
    while current_time <= current_time:
        # Randomly choose a user and an activity
        user = random.choice(users)
        activity = random.choice(activities)
        
        # Append the log entry to the list
        logs.append({'User': user, 'Activity': activity, 'Time': current_time})
        
        # Increment the time by a random number of seconds between 1 and 10
        current_time += timedelta(seconds=random.randint(1, 10))
    
    # Convert the list of logs to a DataFrame
    df = pd.DataFrame(logs)
    
    return df