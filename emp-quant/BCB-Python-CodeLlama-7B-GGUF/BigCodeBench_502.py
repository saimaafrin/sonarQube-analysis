
from datetime import datetime, timedelta
import pandas as pd
import random
import seaborn as sns

def task_func(days_in_past=7, random_seed=0):
    # Set random seed for reproducibility
    random.seed(random_seed)

    # Generate random activity durations for each day
    activity_durations = {}
    for i in range(days_in_past):
        activity_durations[i] = {}
        for activity in ["Running", "Swimming", "Cycling", "Yoga", "Weight Training"]:
            activity_durations[i][activity] = random.randint(0, 120)

    # Create DataFrame from activity durations
    df = pd.DataFrame(activity_durations)
    df.index = pd.date_range(start=datetime.now() - timedelta(days=days_in_past), periods=days_in_past, freq="D")
    df.columns = ["Running", "Swimming", "Cycling", "Yoga", "Weight Training"]

    # Create lineplot with date on x-axis, duration on y-axis, and activity as hue
    ax = sns.lineplot(data=df, x="Date", y="Duration", hue="Activity")

    return ax, df