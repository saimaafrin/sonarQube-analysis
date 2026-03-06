
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI', seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Create a date range based on the start_date, periods, and frequency
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Generate random share prices between 100 and 500
    prices = np.random.uniform(100, 500, size=periods)
    
    # Create a DataFrame with Date and Price columns
    df = pd.DataFrame({'Date': date_range, 'Price': prices})
    
    # Plot the share prices
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Price'], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Share Price')
    ax.set_title('Share Price Series')
    
    return df, ax