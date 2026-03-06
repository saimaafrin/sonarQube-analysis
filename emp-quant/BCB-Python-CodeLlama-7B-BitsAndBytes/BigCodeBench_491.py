
import random
from datetime import datetime
import matplotlib.pyplot as plt

def task_func(epoch_milliseconds, seed=None):
    # Check if the start time is valid
    if epoch_milliseconds < 0 or epoch_milliseconds > datetime.utcnow().timestamp():
        raise ValueError("Invalid start time")

    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)

    # Initialize the sales data dictionary
    sales_data = {}

    # Generate sales data for each category
    for category in ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']:
        sales_data[category] = []
        for day in range(datetime.utcnow().timestamp() - epoch_milliseconds):
            sales_data[category].append(random.randint(10, 50))

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(sales_data['Electronics'], label='Electronics')
    ax.plot(sales_data['Clothing'], label='Clothing')
    ax.plot(sales_data['Home'], label='Home')
    ax.plot(sales_data['Books'], label='Books')
    ax.plot(sales_data['Sports'], label='Sports')
    ax.set_xlabel('Days since start time')
    ax.set_ylabel('Sales units')
    ax.legend()

    return sales_data, ax