
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def task_func(epoch_milliseconds, seed=None):
    # Convert epoch milliseconds to datetime
    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    current_time = datetime.now()
    
    # Check if the start time is negative or after the current time
    if start_time > current_time:
        raise ValueError("Start time is after the current time")
    
    # Define the categories
    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
    
    # Initialize sales data
    sales_data = {category: [] for category in categories}
    
    # Calculate the number of days between start_time and current_time
    days = (current_time - start_time).days
    
    # Generate random sales data for each category
    for _ in range(days):
        for category in categories:
            sales_data[category].append(random.randint(10, 50))
    
    # Plot the sales trend
    fig, ax = plt.subplots()
    for category in categories:
        ax.plot(range(days), sales_data[category], label=category)
    ax.set_xlabel('Days since (start date)')
    ax.set_ylabel('Sales units')
    ax.set_title('Sales Trend by Category')
    ax.legend()
    
    return sales_data, ax