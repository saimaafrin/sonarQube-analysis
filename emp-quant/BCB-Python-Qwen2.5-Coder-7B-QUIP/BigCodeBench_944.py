
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI', seed=0):
    # Set the seed for the random number generator
    np.random.seed(seed)
    
    # Generate a date range
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Generate random share prices between 100 and 500
    share_prices = np.random.uniform(100, 500, size=periods)
    
    # Create a DataFrame with the date range and share prices
    df = pd.DataFrame({'Date': date_range, 'Price': share_prices})
    
    # Plot the share prices
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Price'], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Share Price')
    ax.set_title('Share Price Series')
    
    return df, ax