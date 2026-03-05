import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
START_DATE = '2016-01-01'
PERIODS = 13
FREQ = 'WOM-2FRI'
CATEGORIES = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
def task_func(start_date=START_DATE, periods=PERIODS, freq=FREQ, categories=CATEGORIES):
    # Create a DataFrame with the sales data
    sales_data = pd.DataFrame(
        {
            'Date': pd.date_range(start_date, periods=periods, freq=freq),
            'Category': categories,
            'Sales': np.random.randint(100, 1000, size=(periods, len(categories))),
        }
    )

    # Create a line plot of the sales data
    fig, ax = plt.subplots()
    sales_data.plot(kind='line', x='Date', y='Sales', ax=ax)

    # Add a title and labels to the plot
    ax.set_title('Sales Report')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')

    # Return the Matplotlib Axes object
    return ax