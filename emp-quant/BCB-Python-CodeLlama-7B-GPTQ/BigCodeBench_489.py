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
    """
    # Check if the start time is after the current system time
    if epoch_milliseconds > datetime.now().timestamp() * 1000:
        raise ValueError("Start time is after the current system time")

    # Set the random seed
    random.seed(seed)

    # Initialize the list of logs
    logs = []

    # Iterate from the starting epoch time to the current system time
    for i in range(int(epoch_milliseconds / 1000), int(datetime.now().timestamp() * 1000)):
        # Generate a random user
        user = random.choice(["user1", "user2", "user3", "user4", "user5"])

        # Generate a random activity
        activity = random.choice(["login", "logout", "browse", "search", "purchase"])

        # Generate a random time
        time = i + random.randint(1, 10)

        # Add the log to the list
        logs.append({"User": user, "Activity": activity, "Time": time})

    # Create a DataFrame from the list of logs
    df = pd.DataFrame(logs)

    # Return the DataFrame
    return df