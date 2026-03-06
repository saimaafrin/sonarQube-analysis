
import pandas as pd
from datetime import datetime, timedelta
import random

def task_func(epoch_milliseconds, seed=0):
    # Set the seed for reproducibility
    random.seed(seed)
    
    # Convert epoch milliseconds to datetime object
    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000)
    current_time = datetime.now()
    
    # Check if the start time is after the current system time
    if start_time > current_time:
        raise ValueError("Start time cannot be after the current system time.")
    
    # Predefined lists of users and activities
    users = ['user1', 'user2', 'user3', 'user4', 'user5']
    activities = ['login', 'logout', 'browse', 'search', 'purchase']
    
    # Initialize variables
    logs = []
    current_log_time = start_time
    
    # Generate user activity logs
    while current_log_time <= current_time:
        user = random.choice(users)
        activity = random.choice(activities)
        logs.append({'User': user, 'Activity': activity, 'Time': current_log_time})
        
        # Increment the time by a random number of seconds between 1 and 10
        time_increment = random.randint(1, 10)
        current_log_time += timedelta(seconds=time_increment)
    
    # Create a DataFrame from the logs
    df_logs = pd.DataFrame(logs)
    
    return df_logs