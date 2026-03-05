from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
def task_func(date_str):
    # Convert the input date string to a datetime object
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Extract the day of the month as the frequency of the sine wave
    frequency = date.day
    
    # Generate time points from 0 to 2*pi
    t = np.linspace(0, 2 * np.pi, 1000)
    
    # Calculate the sine wave using the extracted frequency
    y = np.sin(frequency * t)
    
    # Create a figure and an axes object
    fig, ax = plt.subplots()
    
    # Plot the sine wave
    ax.plot(t, y)
    
    # Set the title of the plot
    ax.set_title(f'Sine Wave with Frequency {frequency}')
    
    # Return the axes object
    return ax