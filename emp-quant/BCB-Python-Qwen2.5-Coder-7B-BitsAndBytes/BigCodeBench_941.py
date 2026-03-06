
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_date: str, periods: int, freq: str, random_seed: int = 0) -> (pd.DataFrame, plt.Axes):
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Create a date range
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Generate random sales data
    sales_data = np.cumsum(np.random.normal(size=periods)) * 100
    
    # Create a DataFrame
    df = pd.DataFrame({'Date': date_range, 'Sales': sales_data})
    
    # Plot the sales forecast
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Sales'], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Forecast')
    
    return df, ax