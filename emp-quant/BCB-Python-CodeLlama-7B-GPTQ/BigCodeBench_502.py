from datetime import datetime, timedelta
import pandas as pd
import random
import seaborn as sns
def task_func(days_in_past=7, random_seed=0):
    """
    Generates a graph of daily activity durations for a specified number of days in the past using randomly generated data for activities.

    Parameters
    ----------
    days_in_past : int, optional
        Number of days in the past to generate data for.
        Default is 7.
    random_seed : int, optional
        Random seed to use for generating random data.
        Default is 0.

    Returns
    -------
    ax : matplotlib.pyplot.Axes
        DataFrame used for plotting.
    df : pd.DataFrame
        Seaborn lineplot with date on the x-axis, duration on the y-axis, and activity as hue.
    """
    # Generate random data for activities
    activities = ["Running", "Swimming", "Cycling", "Yoga", "Weight Training"]
    data = []
    for i in range(days_in_past):
        date = datetime.now() - timedelta(days=i)
        for activity in activities:
            duration = random.randint(0, 120)
            data.append({"Date": date, "Activity": activity, "Duration": duration})

    # Create DataFrame
    df = pd.DataFrame(data)

    # Plot data
    ax = sns.lineplot(x="Date", y="Duration", hue="Activity", data=df)

    return ax, df