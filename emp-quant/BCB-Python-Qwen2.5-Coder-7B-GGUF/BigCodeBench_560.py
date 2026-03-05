
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

def task_func(data):
    # Convert the 'date' column to datetime
    data['date'] = pd.to_datetime(data['date'])
    
    # Extract the year from the 'date' column
    year = data['date'].dt.year.iloc[0]
    
    # Set the 'date' column as the index
    data.set_index('date', inplace=True)
    
    # Plot the bar chart
    ax = data['value'].plot(kind='bar', figsize=(10, 6))
    
    # Set the title, x-label, and y-label
    ax.set_title(f'Monthly Data for {year}')
    ax.set_xlabel('Month')
    ax.set_ylabel('Value')
    
    # Return the Axes object
    return ax