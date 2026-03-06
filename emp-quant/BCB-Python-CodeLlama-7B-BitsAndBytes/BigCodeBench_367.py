
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

def task_func(activities):
    # Check if all activities are datetime objects
    if not all(isinstance(activity, datetime) for activity in activities):
        raise TypeError("All activities must be datetime objects")

    # Create a dictionary to store the number of activities per day of the week
    activities_per_day = defaultdict(int)

    # Iterate over the activities and increment the number of activities per day of the week
    for activity in activities:
        activities_per_day[activity.weekday()] += 1

    # Create a bar chart of the number of activities per day of the week
    fig, ax = plt.subplots()
    ax.bar(range(7), activities_per_day.values(), align='center')
    ax.set_xticks(range(7))
    ax.set_xticklabels(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    ax.set_ylabel('Number of Activities')
    ax.set_title('Weekly Activity')
    plt.show()