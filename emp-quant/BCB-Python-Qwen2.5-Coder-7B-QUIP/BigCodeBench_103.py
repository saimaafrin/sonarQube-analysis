
import matplotlib.pyplot as plt
import pandas as pd

def task_func(temperatures):
    # Check if the input DataFrame is not empty
    if temperatures.empty:
        raise ValueError("Input DataFrame is empty")
    
    # Ensure the DataFrame has the expected columns
    expected_columns = ['Date', 'Temperature']
    if not all(column in temperatures.columns for column in expected_columns):
        raise ValueError("Input DataFrame does not have the expected columns")
    
    # Plot the temperature data
    fig, ax = plt.subplots()
    ax.plot(temperatures['Date'], temperatures['Temperature'], 'b-')
    ax.set_xlabel('Date', fontsize=12, fontname='Arial')
    ax.set_ylabel('Temperature (°C)', fontsize=12, fontname='Arial')
    ax.set_title('Daily Temperatures in New York', fontsize=14, fontname='Arial')
    
    # Return the Axes object
    return ax