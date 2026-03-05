from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
def task_func(data):
    """
    Plots a bar chart of monthly data values for a single year.

    Parameters:
    data (pd.DataFrame): A pandas DataFrame with columns 'month' and 'value'.

    Returns:
    matplotlib.axes.Axes: A matplotlib.axes.Axes object representing the plot.
    """
    # Ensure the 'month' column is of datetime type
    data['month'] = pd.to_datetime(data['month'], format='%B')
    
    # Set the year to 2023 for the plot title
    year = 2023
    
    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(data['month'], data['value'], color='blue')
    
    # Set the title, x-label, and y-label
    ax.set_title(f'Monthly Data for {year}')
    ax.set_xlabel('Month')
    ax.set_ylabel('Value')
    
    # Rotate x-axis labels for better readability
    ax.set_xticklabels(data['month'].dt.strftime('%B'), rotation=45)
    
    return ax