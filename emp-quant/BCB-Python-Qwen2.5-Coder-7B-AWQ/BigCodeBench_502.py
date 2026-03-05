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
    
    # Generate data for the specified number of days in the past
    for _ in range(days_in_past):
        # Generate a random date
        date = datetime.now() - timedelta(days=days_in_past + 1 - _)
        
        # Generate random durations for each activity
        durations = {activity: random.randint(0, 120) for activity in activities}
        
        # Append the data to the list
        data.append([date] + list(durations.values()))
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=["Date"] + activities)
    
    # Convert the Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"])
    
    # Set the Date column as the index
    df.set_index("Date", inplace=True)
    
    # Create a Seaborn lineplot
    ax = sns.lineplot(data=df, hue="Activity", y="Duration", x=df.index)
    
    # Return the ax and df
    return ax, df