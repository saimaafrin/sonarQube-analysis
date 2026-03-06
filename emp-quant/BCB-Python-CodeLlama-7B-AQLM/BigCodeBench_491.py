import random
from datetime import datetime
import matplotlib.pyplot as plt
def task_func(epoch_milliseconds, seed=None):
    """
    Generate and draw a sales trend for different categories from a particular epoch milliseconds
    to the current UTC time.

    The function selects category from ['Electronics', 'Clothing', 'Home', 'Books', 'Sports'].
    Each day's sales are randomly determined between 10 and 50 units for each category.
    The plot's x-axis represents 'Days since (the start date)', and the y-axis represents 'Sales' units.

    Parameters:
    - epoch_milliseconds (int): Start time. Must be positive and before current time.
    - seed (int, optional): Seed for random number generation. Default is None (no seed).

    Returns:
    - sales_data (dict): Sales data for different categories over days.
    - ax (plt.Axes): The plot depicting the sales trend.

    Raises:
    - ValueError: If the start time is negative or after the current time.
    
    Requirements:
    - random
    - datetime.datetime
    - matplotlib

    Example:
    >>> random.seed(42)
    >>> sales_data, ax = task_func(1236472051807, seed=42)
    >>> type(sales_data)
    <class 'dict'>
    >>> list(sales_data['Electronics'])[:3]
    [50, 24, 47]
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    if epoch_milliseconds < 0:
        raise ValueError('Start time must be positive.')
    if epoch_milliseconds > datetime.utcnow().timestamp() * 1000:
        raise ValueError('Start time must be before current time.')

    # Generate sales data
    sales_data = {}
    for category in ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']:
        sales_data[category] = []
        for day in range(100):
            sales_data[category].append(random.randint(10, 50))

    # Draw the plot
    fig, ax = plt.subplots()
    ax.set_title('Sales Trend')
    ax.set_xlabel('Days since ' + datetime.utcfromtimestamp(epoch_milliseconds / 1000).strftime('%Y-%m-%d'))
    ax.set_ylabel('Sales Units')
    ax.set_xticks(range(100))
    ax.set_xticklabels(range(100))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.grid(True)
    ax.bar(range(100), sales_data['Electronics'], color='#0000FF', label='Electronics')
    ax.bar(range(100), sales_data['Clothing'], color='#FF0000', label='Clothing')
    ax.bar(range(100), sales_data['Home'], color='#00FF00', label='Home')
    ax.bar(range(100), sales_data['Books'], color='#FF00FF', label='Books')
    ax.bar(range(100), sales_data['Sports'], color='#00FFFF', label='Sports')
    ax.legend()
    return sales_data, ax