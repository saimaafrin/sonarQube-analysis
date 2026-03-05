
from datetime import datetime, timedelta
import pandas as pd
import random
import seaborn as sns

def task_func(days_in_past=7, random_seed=0):
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Define the list of activities
    activities = ["Running", "Swimming", "Cycling", "Yoga", "Weight Training"]
    
    # Create a list to store the data
    data = []
    
    # Loop through each day in the past
    for i in range(days_in_past):
        # Calculate the date for the current day
        date = datetime.now() - timedelta(days=i)
        
        # Loop through each activity
        for activity in activities:
            # Generate a random duration for the current activity
            duration = random.randint(0, 120)
            
            # Append the data for the current activity to the list
            data.append([date, activity, duration])
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=["Date", "Activity", "Duration"])
    
    # Convert the Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"])
    
    # Set the Date column as the index
    df.set_index("Date", inplace=True)
    
    # Create a Seaborn lineplot with date on the x-axis, duration on the y-axis, and activity as hue
    ax = sns.lineplot(data=df, x=df.index, y="Duration", hue="Activity")
    
    # Set the title of the plot
    ax.set_title(f"Daily Activity Durations for the Past {days_in_past} Days")
    
    # Return the ax and df
    return ax, df