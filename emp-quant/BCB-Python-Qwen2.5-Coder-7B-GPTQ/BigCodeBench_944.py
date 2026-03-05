import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI', seed=0):
    """
    Generate a share price series for a specific period of time, plot the share prices, and return the DataFrame and the plot on the share prices over the given date range.
    
    Parameters:
    - start_date (str): The start date of the series in 'YYYY-MM-DD' format.
    - periods (int): The number of periods in the series.
    - freq (str): The frequency of the date range.
    - seed (int): The seed for the random number generator.
    
    Returns:
    - tuple: A tuple containing a pandas DataFrame with columns ['Date', 'Price'] and a Matplotlib Axes object for the plot.
    """
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Create a date range
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Generate random share prices between 100 and 500
    prices = np.random.uniform(100, 500, periods)
    
    # Create a DataFrame
    df = pd.DataFrame({'Date': date_range, 'Price': prices})
    
    # Plot the share prices
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Price'], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title('Share Price Series')
    
    return df, ax