
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
START_DATE = '2016-01-01'
PERIODS = 13
FREQ = 'WOM-2FRI'
CATEGORIES = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']

def task_func(start_date=START_DATE, periods=PERIODS, freq=FREQ, categories=CATEGORIES):
    # Generate a date range
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Initialize a DataFrame with the date range and categories
    data = pd.DataFrame(date_range, columns=['Date'])
    data['Category'] = np.random.choice(categories, size=periods)
    
    # Generate random sales data
    data['Sales'] = np.random.randint(10, 100, size=periods)
    
    # Plot the sales data
    fig, ax = plt.subplots()
    for category in categories:
        ax.plot(data[data['Category'] == category]['Date'], data[data['Category'] == category]['Sales'], label=category)
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Report by Category')
    ax.legend()
    
    return data, ax