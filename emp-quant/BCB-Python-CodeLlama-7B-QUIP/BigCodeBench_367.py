
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

def task_func(activities):
    # Check if all activities are datetime objects
    if not all(isinstance(activity, datetime) for activity in activities):
        raise TypeError("All activities must be datetime objects")

    # Create a dictionary to store the number of activities for each day of the week
    day_of_week_counts = defaultdict(int)

    # Loop through the activities and increment the count for the corresponding day of the week
    for activity in activities:
        day_of_week_counts[activity.weekday()] += 1

    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(day_of_week_counts.keys(), day_of_week_counts.values(), label='Number of Activities')
    ax.set_xlabel('Day of the Week')
    ax.set_ylabel('Number of Activities')
    ax.set_title('Weekly Activity')
    ax.set_xticks(ax.get_xticks()[::2])
    ax.set_xticklabels(ax.get_xticks()[::2])
    fig.tight_layout()

    return ax