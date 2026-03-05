import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
def task_func(epoch_milliseconds, seed=None):
    # Convert epoch milliseconds to datetime
    start_date = datetime.fromtimestamp(epoch_milliseconds / 1000)
    current_date = datetime.utcnow()
    
    # Check if the start time is negative or after the current time
    if start_date < datetime(1970, 1, 1) or start_date > current_date:
        raise ValueError("Start time must be a positive timestamp before the current UTC time.")
    
    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)
    
    # Define the categories
    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
    
    # Calculate the number of days between start_date and current_date
    days = (current_date - start_date).days
    
    # Initialize sales data dictionary
    sales_data = {category: [] for category in categories}
    
    # Generate random sales data for each category for each day
    for _ in range(days):
        for category in categories:
            sales_data[category].append(random.randint(10, 50))
    
    # Create a figure and axis for the plot
    fig, ax = plt.subplots()
    
    # Plot the sales data for each category
    for category in categories:
        ax.plot(sales_data[category], label=category)
    
    # Set the labels and title
    ax.set_xlabel('Days since start date')
    ax.set_ylabel('Sales units')
    ax.set_title('Sales Trend for Different Categories')
    ax.legend()
    
    # Return the sales data and the plot axis
    return sales_data, ax