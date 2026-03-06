
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt

def task_func(days_in_past=7, random_seed=0):
    if days_in_past < 1:
        raise ValueError("days_in_past must be at least 1")
    
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate dates for the last `days_in_past` days
    dates = [datetime.now() - timedelta(days=i) for i in range(days_in_past)]
    
    # Generate random temperatures between 15°C and 35°C
    temperatures = np.random.randint(15, 36, size=days_in_past)
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature Trend')
    
    return ax