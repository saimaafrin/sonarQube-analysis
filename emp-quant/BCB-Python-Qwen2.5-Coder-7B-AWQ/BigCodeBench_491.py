import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
def task_func(epoch_milliseconds, seed=None):
    # Convert epoch milliseconds to datetime
    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000)
    current_time = datetime.utcnow()
    
    # Check if start time is negative or after the current time
    if start_time < datetime(1970, 1, 1) or start_time > current_time:
        raise ValueError("Start time must be non-negative and before the current UTC time.")
    
    # Define categories
    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
    
    # Initialize sales data dictionary
    sales_data = {category: [] for category in categories}
    
    # Generate random sales data for each category
    days = (current_time - start_time).days + 1
    for _ in range(days):
        for category in categories:
            sales_data[category].append(random.randint(10, 50))
    
    # Create a plot
    fig, ax = plt.subplots()
    for category in categories:
        ax.plot(sales_data[category], label=category)
    
    # Set plot labels and title
    ax.set_xlabel('Days since start date')
    ax.set_ylabel('Sales units')
    ax.set_title('Sales Trend for Different Categories')
    ax.legend()
    
    return sales_data, ax