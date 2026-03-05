import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(data):
    # Convert string prices to float values
    data['Price'] = data['Price_String'].str.replace(',', '').astype(float)

    # Calculate statistical measures
    mean = data['Price'].mean()
    median = data['Price'].median()
    std_dev = data['Price'].std()

    # Generate histogram plot
    fig, ax = plt.subplots()
    ax.hist(data['Price'], bins='auto', color='blue', alpha=0.7, rwidth=0.85)
    ax.set_title('Histogram of Product Prices')
    ax.set_xlabel('Price')
    ax.set_ylabel('Frequency')

    # Return results
    return {'mean': mean, 'median': median, 'std_dev': std_dev}, ax
data = {'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
        'Price_String': ['$10.99', '$14.99', '$19.99', '$24.99', '$29.99']}