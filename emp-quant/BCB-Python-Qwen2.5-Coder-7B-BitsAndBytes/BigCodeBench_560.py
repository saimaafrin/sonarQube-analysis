
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

def task_func(data):
    """
    Plots a bar chart of monthly data values for a single year.
    
    Parameters:
    data (pd.DataFrame): A DataFrame containing two columns: 'date' and 'value'.
                         The 'date' column should be in datetime format.
                         The 'value' column contains the data values to be plotted.
    
    Returns:
    matplotlib.axes.Axes: A matplotlib.axes.Axes object representing the plot.
    """
    # Ensure the date column is in datetime format
    data['date'] = pd.to_datetime(data['date'])
    
    # Extract the year from the date column
    year = data['date'].dt.year.unique()[0]
    
    # Group the data by month and sum the values
    monthly_data = data.groupby(data['date'].dt.month)['value'].sum().reset_index()
    monthly_data.columns = ['month', 'value']
    
    # Create the bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(monthly_data['month'], monthly_data['value'], color='skyblue')
    
    # Set the title and labels
    ax.set_title(f'Monthly Data for {year}')
    ax.set_xlabel('Month')
    ax.set_ylabel('Value')
    
    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    
    return ax

    # Plot the data
    ax = task_func(df)
    plt.show()