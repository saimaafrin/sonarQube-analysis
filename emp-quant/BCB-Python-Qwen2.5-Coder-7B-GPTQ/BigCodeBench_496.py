from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
def task_func(days_in_past=7, random_seed=0):
    if days_in_past < 1:
        raise ValueError("days_in_past must be at least 1")
    
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate dates for the past 'days_in_past' days
    dates = [datetime.now() - timedelta(days=i) for i in range(days_in_past)]
    
    # Generate random temperatures between 15 and 35 degrees Celsius
    temperatures = np.random.randint(15, 36, days_in_past)
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, marker='o')
    
    # Set labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature Trend')
    
    # Rotate date labels for better readability
    plt.xticks(rotation=45)
    
    # Return the axes object
    return ax