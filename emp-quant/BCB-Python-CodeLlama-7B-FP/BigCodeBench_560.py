from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
def task_func(data):
    """
    Plots a bar chart of monthly data values for a single year.

    Args:
        data (pd.DataFrame): A pandas DataFrame with columns 'month' and 'value'.

    Returns:
        Axes object: A matplotlib.axes.Axes object representing the plot, with the title formatted as 'Monthly Data for yyyy', x label as 'Month', and y label as 'Value'.
    """
    # Convert the 'month' column to datetime objects
    data['month'] = pd.to_datetime(data['month'], format='%Y-%m')

    # Group the data by month and calculate the sum of 'value' for each month
    data_grouped = data.groupby('month')['value'].sum()

    # Create a bar chart of the data
    fig, ax = plt.subplots()
    ax.bar(data_grouped.index, data_grouped.values)

    # Set the title, x label, and y label of the plot
    ax.set_title(f'Monthly Data for {data.year.iloc[0]}')
    ax.set_xlabel('Month')
    ax.set_ylabel('Value')

    return ax
data = pd.DataFrame({'month': ['2022-01', '2022-02', '2022-03', '2022-04'], 'value': [10, 20, 30, 40]})