
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Constants
START_DATE = '2016-01-01'
PERIODS = 13
FREQ = 'WOM-2FRI'
CATEGORIES = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']

def task_func(start_date=START_DATE, periods=PERIODS, freq=FREQ, categories=CATEGORIES):
    # Create a DataFrame with the sales data
    sales_data = pd.DataFrame({
        'Date': pd.date_range(start_date, periods=periods, freq=freq),
        'Category': categories,
        'Sales': np.random.rand(periods, len(categories))
    })
    # Create a Matplotlib Axes object
    fig, ax = plt.subplots()
    # Plot the sales data
    ax.plot(sales_data['Date'], sales_data['Sales'])
    return ax