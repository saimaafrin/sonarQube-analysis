
import random
from datetime import datetime
import matplotlib.pyplot as plt

def task_func(epoch_milliseconds, seed=None):
    if seed is not None:
        random.seed(seed)
    
    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000)
    current_time = datetime.utcnow()
    
    if epoch_milliseconds < 0 or start_time > current_time:
        raise ValueError("Start time is negative or after the current time.")
    
    days_since_start = (current_time - start_time).days
    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
    sales_data = {category: [] for category in categories}
    
    for day in range(days_since_start + 1):
        for category in categories:
            sales = random.randint(10, 50)
            sales_data[category].append(sales)
    
    days = list(range(days_since_start + 1))
    
    fig, ax = plt.subplots()
    for category in categories:
        ax.plot(days, sales_data[category], label=category)
    
    ax.set_xlabel('Days since (the start date)')
    ax.set_ylabel('Sales units')
    ax.set_title('Sales Trend for Different Categories')
    ax.legend()
    
    return sales_data, ax