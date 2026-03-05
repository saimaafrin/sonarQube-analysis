
import pandas as pd
from datetime import datetime, timedelta
import random

def task_func(epoch_milliseconds, seed=0):
    random.seed(seed)
    start_time = datetime.fromtimestamp(epoch_milliseconds)
    current_time = datetime.now()
    if start_time > current_time:
        raise ValueError("Start time is after the current system time")
    logs = []
    while start_time <= current_time:
        user = random.choice(["user1", "user2", "user3", "user4", "user5"])
        activity = random.choice(["login", "logout", "browse", "search", "purchase"])
        time = start_time + timedelta(seconds=random.randint(1, 10))
        logs.append((user, activity, time))
        start_time = time
    return pd.DataFrame(logs, columns=["User", "Activity", "Time"])