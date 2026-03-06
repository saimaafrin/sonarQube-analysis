
import matplotlib.pyplot as plt
import pandas as pd

def task_func(temperatures):
    """
    Calculate and plot the daytime temperatures for New York over a given period.

    Parameters:
    temperatures (pd.DataFrame): A DataFrame with columns ['date'] and ['temperature'].

    Returns:
    matplotlib.axes.Axes: The Axes object containing the temperature plot.
    """
    # Check if the input DataFrame is empty
    if temperatures.empty:
        raise ValueError("Input DataFrame is empty.")
    
    # Check if the required columns exist
    required_columns = {'date', 'temperature'}
    if not required_columns.issubset(temperatures.columns):
        raise ValueError("Input DataFrame must contain 'date' and 'temperature' columns.")
    
    # Convert the 'date' column to datetime
    temperatures['date'] = pd.to_datetime(temperatures['date'])
    
    # Set the date column as the index
    temperatures.set_index('date', inplace=True)
    
    # Plot the temperatures
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(temperatures.index, temperatures['temperature'], label='Daily Temperature')
    
    # Set the labels and title
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Temperature (°C)', fontsize=14)
    ax.set_title('Daily Temperatures in New York', fontsize=16)
    
    # Set the font to Arial
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontname('Arial')
    
    # Show legend
    ax.legend()
    
    return ax