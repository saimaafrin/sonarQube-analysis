import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
START_DATE = '2016-01-01'
PERIODS = 13
FREQ = 'WOM-2FRI'
CATEGORIES = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
def task_func(start_date=START_DATE, periods=PERIODS, freq=FREQ, categories=CATEGORIES):
    """
    Create and visualize a sales report for different categories over a period of time.

    Returns a DataFrame containing the sales data with the following columns: 'Date', 'Category', 'Sales'.
    Returns the Matplotlib Axes object for the plot.
    """
    # Generate random sales data
    sales_data = []
    for i in range(periods):
        date = start_date + pd.DateOffset(weeks=i)
        for category in categories:
            sales = np.random.randint(100, 1000)
            sales_data.append({'Date': date, 'Category': category, 'Sales': sales})

    # Create a DataFrame from the sales data
    sales_df = pd.DataFrame(sales_data)

    # Group the DataFrame by category and date
    grouped_df = sales_df.groupby(['Category', 'Date'])['Sales'].sum()

    # Create a line plot of the sales data
    fig, ax = plt.subplots()
    ax.plot(grouped_df.index, grouped_df['Sales'], label='Sales')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Report')
    ax.legend()

    return grouped_df, ax