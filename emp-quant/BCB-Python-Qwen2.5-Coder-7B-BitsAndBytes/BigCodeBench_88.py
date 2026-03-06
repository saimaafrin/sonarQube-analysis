
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def task_func(start_date, end_date, seed=42):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Convert input strings to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    # Calculate the number of days between the start and end dates
    num_days = (end_date - start_date).days + 1
    
    # Generate random sales data
    sales_data = np.random.randint(0, 501, size=num_days)
    
    # Create a date range from start_date to end_date
    date_range = pd.date_range(start=start_date, periods=num_days)
    
    # Create a DataFrame with Date and Sales columns
    df = pd.DataFrame({'Date': date_range, 'Sales': sales_data})
    
    # Plot the sales data
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Sales'], marker='o', linestyle='-')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Daily Sales Data')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return df, ax