
from datetime import datetime, timedelta
import pandas as pd
import random
import seaborn as sns

def task_func(days_in_past=7, random_seed=0):
    # Set the random seed for reproducibility
    random.seed(random_seed)

    # Define the list of activities
    activities = ["Running", "Swimming", "Cycling", "Yoga", "Weight Training"]

    # Create a list of dates
    dates = [datetime.now() - timedelta(days=i) for i in range(days_in_past)]

    # Create a list of durations
    durations = [random.randint(0, 120) for _ in range(days_in_past)]

    # Create a list of activities
    activity = random.choice(activities)

    # Create a list of data
    data = list(zip(dates, activity, durations))

    # Create a DataFrame
    df = pd.DataFrame(data, columns=["Date", "Activity", "Duration"])

    # Create a lineplot
    ax = sns.lineplot(x="Date", y="Duration", hue="Activity", data=df)

    # Return the plot and the DataFrame
    return ax, df