from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
def task_func(days_in_past=7, random_seed=0):
    """
    Generates a graph of temperature trends over the past week using randomly generated data.

    Parameters:
    days_in_past (int): Number of days in the past to generate data for. Must be at least 1.
    random_seed (int): Seed for the random number generator for reproducibility.

    Returns:
    ax (matplotlib.axes._axes.Axes): Generated plot showing 'Temperature Trend'
    with 'Date' on the x-axis and 'Temperature (°C)' on the y-axis.

    Raises:
    ValueError: If days_in_past is less than 1.
    """
    if days_in_past < 1:
        raise ValueError("days_in_past must be at least 1")

    # Set the random seed for reproducibility
    np.random.seed(random_seed)

    # Generate dates
    dates = [datetime.now() - timedelta(days=i) for i in range(days_in_past)]

    # Generate random temperatures between 15 and 35 degrees Celsius
    temperatures = np.random.randint(15, 36, size=days_in_past)

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature Trend')

    return ax