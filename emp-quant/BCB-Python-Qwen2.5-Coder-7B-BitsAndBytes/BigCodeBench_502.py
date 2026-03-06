
from datetime import datetime, timedelta
import pandas as pd
import random
import seaborn as sns

def task_func(days_in_past=7, random_seed=0):
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Define the list of activities
    activities = ["Running", "Swimming", "Cycling", "Yoga", "Weight Training"]
    
    # Create an empty list to store the data
    data = []
    
    # Loop through the number of days in the past
    for i in range(days_in_past):
        # Calculate the date for the current day
        date = datetime.now() - timedelta(days=i)
        
        # Loop through the list of activities
        for activity in activities:
            # Generate a random duration between 0 and 120
            duration = random.randint(0, 120)
            
            # Append the data to the list
            data.append([date, activity, duration])
    
    # Convert the list of data to a DataFrame
    df = pd.DataFrame(data, columns=["Date", "Activity", "Duration"])
    
    # Sort the DataFrame by date
    df.sort_values(by="Date", inplace=True)
    
    # Create a line plot using Seaborn
    ax = sns.lineplot(x="Date", y="Duration", hue="Activity", data=df)
    
    # Return the Axes object and the DataFrame
    return ax, df