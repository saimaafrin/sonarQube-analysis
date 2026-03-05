
import pandas as pd
from datetime import datetime, timedelta
import random

def task_func(epoch_milliseconds, seed=0):
    # Check if the start time is after the current system time
    if epoch_milliseconds > (datetime.now() - timedelta(seconds=1)).timestamp():
        raise ValueError("Start time is after the current system time")

    # Generate user activity logs
    logs = []
    current_time = datetime.fromtimestamp(epoch_milliseconds)
    while current_time < datetime.now():
        user = random.choice(["user1", "user2", "user3", "user4", "user5"])
        activity = random.choice(["login", "logout", "browse", "search", "purchase"])
        logs.append({"User": user, "Activity": activity, "Time": current_time})
        current_time += timedelta(seconds=random.randint(1, 10))

    # Create a DataFrame from the logs
    df = pd.DataFrame(logs)

    return df