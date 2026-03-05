from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
def task_func(date_str):
    """
    Plots a sine wave whose frequency is determined by the day of the month from the given date.
    
    Parameters:
    - date_str (str): A string representing the date in the format 'YYYY-MM-DD'.
    
    Returns:
    - matplotlib.axes.Axes: An Axes object containing the plotted sine wave.
    """
    # Convert the date string to a datetime object
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Extract the day of the month
    day_of_month = date.day
    
    # Generate time points
    t = np.linspace(0, 2 * np.pi, 1000)
    
    # Calculate the frequency based on the day of the month
    frequency = day_of_month / 30.0  # Assuming 30 days in a month for simplicity
    
    # Calculate the sine wave
    y = np.sin(frequency * t)
    
    # Create a figure and an axes
    fig, ax = plt.subplots()
    
    # Plot the sine wave
    ax.plot(t, y)
    
    # Set the title and labels
    ax.set_title(f'Sine Wave with Frequency Based on Day of the Month ({day_of_month})')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    
    # Return the axes object
    return ax