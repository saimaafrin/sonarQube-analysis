from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
def task_func(date_str):
    # Convert the input date string to a datetime object
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Extract the day of the month from the date
    day_of_month = date_obj.day
    
    # Generate time points from 0 to 2*pi
    t = np.linspace(0, 2 * np.pi, 1000)
    
    # Calculate the frequency of the sine wave based on the day of the month
    frequency = day_of_month / 30.0  # Assuming 30 days in a month for simplicity
    
    # Generate the sine wave
    y = np.sin(frequency * t)
    
    # Create a figure and an axes object
    fig, ax = plt.subplots()
    
    # Plot the sine wave
    ax.plot(t, y)
    
    # Set the title of the plot
    ax.set_title(f'Sine Wave with Frequency Based on Day of the Month ({day_of_month})')
    
    # Return the axes object
    return ax