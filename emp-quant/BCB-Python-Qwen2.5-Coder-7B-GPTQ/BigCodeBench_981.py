import pandas as pd
from datetime import datetime, timedelta
import random
import matplotlib.pyplot as plt
def task_func(start_date, end_date, num_series, seed=None):
    """
    Generates a DataFrame with multiple random integer time series and plots them on a line plot.
    
    Parameters:
    - start_date (str): The start date in 'YYYY-MM-DD' format.
    - end_date (str): The end date in 'YYYY-MM-DD' format.
    - num_series (int): The number of time series to generate.
    - seed (int, optional): Seed for random number generation for reproducibility.
    
    Returns:
    - pandas.DataFrame: A DataFrame containing the generated time series, indexed by date.
    - plt.Axes: A matplotlib line plot of the time series.
    """
    # Validate input parameters
    if start_date > end_date:
        raise ValueError("start_date must be earlier than end_date")
    if num_series < 1:
        raise ValueError("num_series must be at least 1")
    
    # Set random seed if provided
    if seed is not None:
        random.seed(seed)
    
    # Convert start and end dates to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    # Calculate the number of days between start and end dates
    num_days = (end_date - start_date).days + 1
    
    # Initialize an empty DataFrame
    df = pd.DataFrame(index=pd.date_range(start=start_date, periods=num_days))
    
    # Generate random time series
    for i in range(num_series):
        series_name = f"series_{i+1}"
        df[series_name] = [random.randint(0, 100) for _ in range(num_days)]
    
    # Plot the time series
    fig, ax = plt.subplots()
    for column in df.columns:
        ax.plot(df.index, df[column], label=column)
    
    # Set plot title and labels
    ax.set_title("Random Time Series")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    
    # Add legend
    ax.legend()
    
    return df, ax