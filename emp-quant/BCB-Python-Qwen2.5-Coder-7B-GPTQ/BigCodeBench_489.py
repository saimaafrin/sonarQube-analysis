import pandas as pd
from datetime import datetime, timedelta
import random
def task_func(epoch_milliseconds, seed=0):
    # Set the seed for reproducibility
    random.seed(seed)
    
    # Convert epoch time to datetime
    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000)
    
    # Get the current system time
    current_time = datetime.now()
    
    # Check if the start time is after the current system time
    if start_time > current_time:
        raise ValueError("Start time cannot be after the current system time.")
    
    # Define user and activity lists
    users = ['user1', 'user2', 'user3', 'user4', 'user5']
    activities = ['login', 'logout', 'browse', 'search', 'purchase']
    
    # Initialize variables
    logs = []
    current_time = start_time
    
    # Generate logs
    while current_time <= current_time:
        user = random.choice(users)
        activity = random.choice(activities)
        logs.append({'User': user, 'Activity': activity, 'Time': current_time})
        # Increment time by a random number of seconds between 1 and 10
        current_time += timedelta(seconds=random.randint(1, 10))
    
    # Convert logs to DataFrame
    df = pd.DataFrame(logs)
    
    return df