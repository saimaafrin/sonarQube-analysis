from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
def task_func(data):
    """
    Plots a bar chart of monthly data values for a single year.

    Parameters:
    data (list of tuples): A list where each tuple contains a datetime object and a value.

    Returns:
    matplotlib.axes.Axes: A matplotlib.axes.Axes object representing the plot.
    """
    # Convert the list of tuples into a pandas DataFrame
    df = pd.DataFrame(data, columns=['date', 'value'])
    
    # Extract the year from the dates
    year = df['date'].dt.year.iloc[0]
    
    # Set the index to the month
    df.set_index(df['date'].dt.month, inplace=True)
    
    # Plot the bar chart
    ax = df['value'].plot(kind='bar', figsize=(10, 6))
    
    # Set the title, x-label, and y-label
    ax.set_title(f'Monthly Data for {year}')
    ax.set_xlabel('Month')
    ax.set_ylabel('Value')
    
    return ax