
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
START_DATE = '2016-01-01'
PERIODS = 13
FREQ = 'WOM-2FRI'
CATEGORIES = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']

def task_func(start_date=START_DATE, periods=PERIODS, freq=FREQ, categories=CATEGORIES):
    # Create a date range
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Initialize an empty DataFrame
    sales_data = pd.DataFrame(columns=['Date', 'Category', 'Sales'])
    
    # Populate the DataFrame with random sales data
    for date in date_range:
        for category in categories:
            sales = np.random.randint(100, 1000)
            sales_data = sales_data.append({'Date': date, 'Category': category, 'Sales': sales}, ignore_index=True)
    
    # Plotting the sales data
    fig, ax = plt.subplots(figsize=(10, 6))
    for category in categories:
        category_data = sales_data[sales_data['Category'] == category]
        ax.plot(category_data['Date'], category_data['Sales'], label=category)
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Report by Category')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return sales_data, ax