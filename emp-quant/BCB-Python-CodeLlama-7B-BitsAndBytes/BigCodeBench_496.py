
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt

def task_func(days_in_past=7, random_seed=0):
    if days_in_past < 1:
        raise ValueError("'days_in_past' must be greater than or equal to 1")

    # Generate random temperatures
    np.random.seed(random_seed)
    temperatures = np.random.randint(15, 35, size=days_in_past)

    # Create a date range for the x-axis
    date_range = [datetime.today() - timedelta(days=i) for i in range(days_in_past)]

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the temperatures
    ax.plot(date_range, temperatures)

    # Set the title and labels
    ax.set_title("Temperature Trend")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")

    # Return the axis object
    return ax