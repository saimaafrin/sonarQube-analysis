import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
START_DATE = '2016-01-01'
PERIODS = 13
FREQ = 'WOM-2FRI'
CATEGORIES = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
def task_func(start_date=START_DATE, periods=PERIODS, freq=FREQ, categories=CATEGORIES):
    """
    Generates a sales report for different categories over a period of time.
    
    Parameters:
    - start_date (str): The start date of the period.
    - periods (int): The number of periods.
    - freq (str): The frequency of the periods.
    - categories (list): The list of categories.
    
    Returns:
    - DataFrame: A DataFrame containing the sales data with columns 'Date', 'Category', 'Sales'.
    - Axes: The Matplotlib Axes object for the plot.
    """
    # Generate dates
    dates = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Generate sales data
    np.random.seed(0)  # For reproducibility
    sales_data = np.random.randint(100, 1000, size=(periods, len(categories)))
    
    # Create DataFrame
    df = pd.DataFrame(sales_data, columns=categories, index=dates)
    df = df.stack().reset_index()
    df.columns = ['Date', 'Category', 'Sales']
    
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    for category in categories:
        ax.plot(df[df['Category'] == category]['Date'], df[df['Category'] == category]['Sales'], label=category)
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Report by Category')
    ax.legend()
    
    return df, ax