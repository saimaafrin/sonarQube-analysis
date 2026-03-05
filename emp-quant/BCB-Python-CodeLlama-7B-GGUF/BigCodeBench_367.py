
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

def task_func(activities):
    if not all(isinstance(activity, datetime) for activity in activities):
        raise TypeError("Activities must be datetime objects")

    # Group activities by day of the week
    activities_by_day = defaultdict(list)
    for activity in activities:
        activities_by_day[activity.weekday()].append(activity)

    # Create bar chart
    fig, ax = plt.subplots()
    ax.bar(range(7), [len(activities_by_day[day]) for day in range(7)])
    ax.set_xlabel("Day of the Week")
    ax.set_ylabel("Number of Activities")
    ax.set_title("Weekly Activity")
    return ax