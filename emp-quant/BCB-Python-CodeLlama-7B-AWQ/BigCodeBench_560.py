from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
def task_func(data):
    """
    Plots a bar chart of monthly data values for a single year.

    Args:
        data (pandas.DataFrame): A pandas DataFrame with columns 'month' and 'value'.

    Returns:
        Axes object: A matplotlib.axes.Axes object representing the plot, with the title formatted as 'Monthly Data for yyyy', x label as 'Month', and y label as 'Value'.
    """
    # Create a new figure and axis object
    fig, ax = plt.subplots()

    # Set the title of the plot
    ax.set_title(f'Monthly Data for {data["year"].iloc[0]}')

    # Set the x-axis label
    ax.set_xlabel('Month')

    # Set the y-axis label
    ax.set_ylabel('Value')

    # Plot the data as a bar chart
    ax.bar(data['month'], data['value'])

    # Return the axis object
    return ax
data = pd.DataFrame({'month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                     'value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]})