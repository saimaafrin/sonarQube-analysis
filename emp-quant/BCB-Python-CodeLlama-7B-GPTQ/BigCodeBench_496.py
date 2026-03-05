from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
def task_func(days_in_past=7, random_seed=0):
    """
    Draw a graph of temperature trends over the past week using randomly generated data.
    This function generates random integer temperatures in Celcius with a low of 15 and high of 35.
    To show temperature trend, it plots date on the x-axis and temperature on the y-axis.
    The function should raise the exception for: ValueError: If days_in_past is less than 1.
    The function should output with:
        ax (matplotlib.axes._axes.Axes): Generated plot showing 'Temperature Trend'
        with 'Date' on the a-xis and 'Temperature (°C)' on the y-axis.
    """
    if days_in_past < 1:
        raise ValueError("days_in_past must be greater than 0")

    # Generate random temperatures
    np.random.seed(random_seed)
    temperatures = np.random.randint(15, 35, size=days_in_past)

    # Create a date range for the x-axis
    date_range = [datetime.now() - timedelta(days=i) for i in range(days_in_past)]

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the temperatures
    ax.plot(date_range, temperatures)

    # Set the x-axis label
    ax.set_xlabel("Date")

    # Set the y-axis label
    ax.set_ylabel("Temperature (°C)")

    # Set the title
    ax.set_title("Temperature Trend")

    # Return the axis object
    return ax
days_in_past = 7
random_seed = 0