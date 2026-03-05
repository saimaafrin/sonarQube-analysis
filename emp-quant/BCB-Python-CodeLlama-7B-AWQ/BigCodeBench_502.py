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
    random_seed : int, optional
        Random seed to use for generating random data.

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
    for day in range(days_in_past):
        activity_durations[day] = {}
        for activity in ["Running", "Swimming", "Cycling", "Yoga", "Weight Training"]:
            activity_durations[day][activity] = random.randint(0, 120)

    # Create DataFrame with activity durations
    df = pd.DataFrame(activity_durations, index=pd.date_range(start=datetime.now() - timedelta(days=days_in_past), end=datetime.now()))

    # Create lineplot with date on x-axis, duration on y-axis, and activity as hue
    ax = sns.lineplot(data=df, x="index", y="value", hue="activity")

    return ax, df
days_in_past = 7
random_seed = 0