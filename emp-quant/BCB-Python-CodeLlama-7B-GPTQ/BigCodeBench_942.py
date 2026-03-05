import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
START_DATE = '2016-01-01'
PERIODS = 13
FREQ = 'WOM-2FRI'
CATEGORIES = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
def task_func(start_date=START_DATE, periods=PERIODS, freq=FREQ, categories=CATEGORIES):
    # Generate random sales data
    sales_data = pd.DataFrame(
        np.random.randint(100, size=(periods, len(categories))),
        columns=['Sales']
    )
    sales_data['Date'] = pd.date_range(start=start_date, periods=periods, freq=freq)
    sales_data['Category'] = categories

    # Plot the sales data
    fig, ax = plt.subplots()
    ax.plot(sales_data['Date'], sales_data['Sales'], label='Sales')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Report')
    ax.legend()

    return sales_data, ax