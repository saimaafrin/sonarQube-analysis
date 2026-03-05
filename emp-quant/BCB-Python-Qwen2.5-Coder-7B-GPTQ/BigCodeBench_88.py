import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
def task_func(start_date, end_date, seed=42):
    """
    Generate random sales data for each day between a start and end date, inclusive.
    
    Parameters:
    start_date (str): The start date in 'YYYY-MM-DD' format.
    end_date (str): The end date in 'YYYY-MM-DD' format.
    seed (int): The seed for the random number generator for reproducibility.
    
    Returns:
    DataFrame: A pandas DataFrame with columns 'Date' and 'Sales'.
    Axes: A matplotlib Axes object of the plot showing the sales overtime.
    """
    # Convert start and end dates to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate dates
    dates = pd.date_range(start=start_date, end=end_date)
    
    # Generate random sales data
    sales = np.random.randint(0, 501, size=len(dates))
    
    # Create DataFrame
    df = pd.DataFrame({'Date': dates, 'Sales': sales})
    
    # Plot the sales data
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Sales'], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Over Time')
    
    return df, ax