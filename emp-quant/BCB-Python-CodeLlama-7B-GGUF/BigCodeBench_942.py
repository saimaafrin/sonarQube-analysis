
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
START_DATE = '2016-01-01'
PERIODS = 13
FREQ = 'WOM-2FRI'
CATEGORIES = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']

def task_func(start_date=START_DATE, periods=PERIODS, freq=FREQ, categories=CATEGORIES):
    # Generate random sales data
    sales_data = np.random.randint(100, size=(len(categories), periods))

    # Create a DataFrame with the sales data
    sales_df = pd.DataFrame(sales_data, columns=['Sales'])
    sales_df['Date'] = pd.date_range(start_date, periods=periods, freq=freq)
    sales_df['Category'] = categories

    # Plot the sales data
    fig, ax = plt.subplots()
    ax.plot(sales_df['Date'], sales_df['Sales'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Report')

    return sales_df, ax

# Call the function and get the DataFrame and Axes object
sales_df, ax = task_func()

# Visualize the sales data
ax.legend(loc='upper left')
plt.show()