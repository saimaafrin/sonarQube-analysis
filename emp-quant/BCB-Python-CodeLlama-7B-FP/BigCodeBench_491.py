import random
from datetime import datetime
import matplotlib.pyplot as plt
def task_func(epoch_milliseconds, seed=None):
    """
    Generate and draw a sales trend for different categories from a particular epoch milliseconds to the current UTC time.
    The function selects category from ['Electronics', 'Clothing', 'Home', 'Books', 'Sports'].
    Each day's sales are randomly determined between 10 and 50 units for each category.
    The plot's x-axis represents 'Days since (the start date)', and the y-axis represents 'Sales' units.
    The function should raise the exception for: ValueError: If the start time is negative or after the current time.
    The function should output with:
        sales_data (dict): Sales data for different categories over days.
        ax (plt.Axes): The plot depicting the sales trend.
    """
    if epoch_milliseconds < 0 or epoch_milliseconds > datetime.now().timestamp() * 1000:
        raise ValueError("Start time must be positive and before the current time.")

    # Generate sales data for each category
    sales_data = {}
    for category in ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']:
        sales_data[category] = []
        for day in range(epoch_milliseconds, datetime.now().timestamp() * 1000, 86400000):
            sales_data[category].append(random.randint(10, 50))

    # Plot the sales trend
    fig, ax = plt.subplots()
    ax.set_xlabel("Days since start date")
    ax.set_ylabel("Sales units")
    ax.set_title("Sales Trend")
    ax.grid(True)
    for category in sales_data:
        ax.plot(sales_data[category], label=category)
    ax.legend()

    return sales_data, ax