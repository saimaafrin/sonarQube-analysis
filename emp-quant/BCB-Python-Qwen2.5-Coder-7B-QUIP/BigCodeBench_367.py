
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

def task_func(activities):
    # Check if all activities are datetime objects
    if not all(isinstance(activity, datetime) for activity in activities):
        raise TypeError("All activities must be datetime objects")
    
    # Initialize a dictionary to count activities per day of the week
    activity_counts = defaultdict(int)
    
    # Count the activities per day of the week
    for activity in activities:
        day_of_week = activity.strftime('%A')
        activity_counts[day_of_week] += 1
    
    # Get the days of the week in order
    days_of_week = sorted(activity_counts.keys())
    
    # Get the number of activities for each day
    activity_counts = [activity_counts[day] for day in days_of_week]
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(days_of_week, activity_counts, width=0.8, align='center')
    ax.set_xlabel('Day of the Week')
    ax.set_ylabel('Number of Activities')
    ax.set_title('Weekly Activity')
    
    return ax