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
    # Set random seed for reproducibility
    random.seed(random_seed)

    # Generate random activity durations for each day
    activity_durations = {}
    for i in range(days_in_past):
        activity_durations[f"{i}"] = {
            "Running": random.randint(0, 120),
            "Swimming": random.randint(0, 120),
            "Cycling": random.randint(0, 120),
            "Yoga": random.randint(0, 120),
            "Weight Training": random.randint(0, 120),
        }

    # Create DataFrame with activity durations
    df = pd.DataFrame(activity_durations)

    # Convert dates to datetime objects
    df["Date"] = pd.to_datetime(df.index, format="%Y-%m-%d")

    # Create lineplot with date on x-axis, duration on y-axis, and activity as hue
    ax = sns.lineplot(data=df, x="Date", y="Duration", hue="Activity")

    return ax, df
days_in_past = 7
random_seed = 0