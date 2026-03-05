
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(data):
    # Convert string prices to float values
    data['Price'] = data['Price'].str.replace(',', '').astype(float)
    
    # Calculate statistical measures
    mean = data['Price'].mean()
    median = data['Price'].median()
    std_dev = data['Price'].std()
    
    # Generate histogram
    fig, ax = plt.subplots()
    ax.hist(data['Price'], bins='auto', color='blue', alpha=0.7, rwidth=0.85)
    ax.set_title('Histogram of Product Prices')
    ax.set_xlabel('Price')
    ax.set_ylabel('Frequency')
    plt.show()
    
    # Return results
    return {'mean': mean, 'median': median, 'std_dev': std_dev}, fig