
import matplotlib.pyplot as plt
import pandas as pd
def task_func(temperatures):
    # Check if the input DataFrame is not in the expected format or empty
    if not temperatures.empty:
        raise ValueError("The input DataFrame is not in the expected format or empty")

    # Calculate the daytime temperatures for New York
    daytime_temperatures = temperatures.loc[temperatures['time'] > 12]

    # Plot the daytime temperatures
    fig, ax = plt.subplots()
    ax.plot(daytime_temperatures['date'], daytime_temperatures['temperature'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Daily Temperatures in New York')
    ax.set_facecolor('white')
    ax.set_font('Arial')
    return ax