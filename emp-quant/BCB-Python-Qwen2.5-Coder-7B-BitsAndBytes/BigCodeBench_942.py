
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
START_DATE = '2016-01-01'
PERIODS = 13
FREQ = 'WOM-2FRI'
CATEGORIES = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']

def task_func(start_date=START_DATE, periods=PERIODS, freq=FREQ, categories=CATEGORIES):
    # Create date range
    dates = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Initialize an empty list to store data
    data = []
    
    # Generate random sales data for each category
    for category in categories:
        sales = np.random.randint(100, 1000, size=periods)
        data.extend(zip(dates, [category] * periods, sales))
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Date', 'Category', 'Sales'])
    
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    for category in categories:
        category_data = df[df['Category'] == category]
        ax.plot(category_data['Date'], category_data['Sales'], marker='o', label=category)
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Report Over Time')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return df, ax