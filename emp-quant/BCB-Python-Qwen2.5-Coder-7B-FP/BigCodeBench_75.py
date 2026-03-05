import pandas as pd
import numpy as np
import itertools
from datetime import datetime, timedelta
import seaborn as sns
def task_func(df, fruits=None, days=None, seed=None, sales_lower_bound=1, sales_upper_bound=50):
    # Check if df is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    
    # Check if df is empty
    if not df.empty:
        raise ValueError("df must be empty")
    
    # Check if sales_lower_bound is less than sales_upper_bound
    if sales_lower_bound >= sales_upper_bound:
        raise ValueError("sales_lower_bound must be less than sales_upper_bound")
    
    # Set the random seed if provided
    if seed is not None:
        np.random.seed(seed)
    
    # Define the date range
    start_date = datetime.now()
    end_date = start_date + timedelta(days=days)
    date_range = pd.date_range(start=start_date, end=end_date)
    
    # Define the fruits if not provided
    if fruits is None:
        fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    
    # Generate random sales data
    sales_data = {}
    for fruit in fruits:
        sales_data[fruit] = np.random.randint(sales_lower_bound, sales_upper_bound, size=len(date_range))
    
    # Create a DataFrame from the sales data
    sales_df = pd.DataFrame(sales_data, index=date_range)
    
    # Append the sales data to the input DataFrame
    df = pd.concat([df, sales_df], axis=1)
    
    # Create a seaborn boxplot of the sales
    boxplot = sns.boxplot(data=sales_df)
    
    # Return the updated DataFrame and the boxplot
    return df, boxplot