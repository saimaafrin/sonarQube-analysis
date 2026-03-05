
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def task_func(start_date, end_date, seed=42):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Convert start_date and end_date to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    # Generate a date range
    date_range = pd.date_range(start=start_date, end=end_date)
    
    # Generate random sales data
    sales_data = np.random.randint(0, 501, size=len(date_range))
    
    # Create a DataFrame
    df = pd.DataFrame({'Date': date_range, 'Sales': sales_data})
    
    # Plot the sales data
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Sales'], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Data Over Time')
    
    return df, ax