
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

def task_func(activities):
    if not all(isinstance(activity, datetime) for activity in activities):
        raise TypeError("All elements in the activities list must be datetime objects.")
    
    # Create a dictionary to count activities per day of the week
    activity_count = defaultdict(int)
    for activity in activities:
        day_of_week = activity.strftime('%A')
        activity_count[day_of_week] += 1
    
    # Prepare data for plotting
    days = list(activity_count.keys())
    counts = list(activity_count.values())
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(days, counts, color='blue')
    
    # Set labels and title
    ax.set_xlabel('Day of the Week')
    ax.set_ylabel('Number of Activities')
    ax.set_title('Weekly Activity')
    
    return ax