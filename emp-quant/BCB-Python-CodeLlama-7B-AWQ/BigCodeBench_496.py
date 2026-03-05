from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
def task_func(days_in_past=7, random_seed=0):
    """
    Draw a graph of temperature trends over the past week using randomly generated data.
    This function generates random integer temperatures in Celcius with a low of 15 and high of 35.
    To show temperature trend, it plots date on the x-axis and temperature on the y-axis.
    """
    if days_in_past < 1:
        raise ValueError("ValueError: days_in_past must be greater than 1")

    # Generate random temperatures
    np.random.seed(random_seed)
    temperatures = np.random.randint(15, 35, size=days_in_past)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the temperatures
    ax.plot(temperatures)

    # Set the x-axis label
    ax.set_xlabel("Date")

    # Set the y-axis label
    ax.set_ylabel("Temperature (°C)")

    # Set the title
    ax.set_title("Temperature Trend")

    return ax