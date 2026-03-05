from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
def task_func(activities):
    """
    Return a bar chart of the number of activities performed on each day of the week based on the provided list of activities.
    If the activities are not datetime objects, raise a TypeError.
    """
    if not all(isinstance(activity, datetime) for activity in activities):
        raise TypeError("The activities must be datetime objects.")

    # Group activities by day of the week
    activities_by_day = defaultdict(list)
    for activity in activities:
        activities_by_day[activity.weekday()].append(activity)

    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(range(7), [len(activities_by_day[day]) for day in range(7)])
    ax.set_xticks(range(7))
    ax.set_xticklabels(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    ax.set_ylabel("Number of Activities")
    ax.set_title("Weekly Activity")
    return ax
activities = [
    datetime(2022, 1, 1, 10, 0),
    datetime(2022, 1, 2, 12, 0),
    datetime(2022, 1, 3, 14, 0),
    datetime(2022, 1, 4, 16, 0),
    datetime(2022, 1, 5, 18, 0),
    datetime(2022, 1, 6, 20, 0),
    datetime(2022, 1, 7, 22, 0),
]