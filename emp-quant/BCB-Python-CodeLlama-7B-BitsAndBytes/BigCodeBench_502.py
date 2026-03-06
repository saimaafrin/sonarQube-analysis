
from datetime import datetime, timedelta
import pandas as pd
import random
import seaborn as sns

def task_func(days_in_past=7, random_seed=0):
    # Generate random activity durations for each activity
    activity_durations = {
        "Running": random.randint(0, 120),
        "Swimming": random.randint(0, 120),
        "Cycling": random.randint(0, 120),
        "Yoga": random.randint(0, 120),
        "Weight Training": random.randint(0, 120)
    }

    # Generate a DataFrame with date, activity, and duration columns
    df = pd.DataFrame(columns=["Date", "Activity", "Duration"])
    for i in range(days_in_past):
        date = datetime.today() - timedelta(days=i)
        for activity, duration in activity_durations.items():
            df = df.append({"Date": date, "Activity": activity, "Duration": duration}, ignore_index=True)

    # Plot the data using seaborn
    ax = sns.lineplot(data=df, x="Date", y="Duration", hue="Activity")

    return (ax, df)