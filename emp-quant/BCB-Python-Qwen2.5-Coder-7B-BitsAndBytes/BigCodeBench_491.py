
import random
from datetime import datetime
import matplotlib.pyplot as plt

def task_func(epoch_milliseconds, seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Convert epoch milliseconds to datetime object
    start_date = datetime.fromtimestamp(epoch_milliseconds / 1000)
    current_date = datetime.utcnow()
    
    if start_date < datetime(1970, 1, 1) or start_date > current_date:
        raise ValueError("Start time must be non-negative and before the current UTC time.")
    
    # Calculate the number of days between start_date and current_date
    num_days = (current_date - start_date).days
    
    # Define categories
    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
    
    # Initialize sales data dictionary
    sales_data = {category: [random.randint(10, 50) for _ in range(num_days)] for category in categories}
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot sales data for each category
    for category, sales in sales_data.items():
        ax.plot(sales, label=category)
    
    # Set labels and title
    ax.set_xlabel('Days since {}'.format(start_date.strftime('%Y-%m-%d')))
    ax.set_ylabel('Sales units')
    ax.set_title('Sales Trend Over Time')
    ax.legend()
    
    return sales_data, ax