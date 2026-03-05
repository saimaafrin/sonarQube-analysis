
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
    
    # Generate sales data for specified fruits over a given range of days
    if fruits is None:
        fruits = ['Apple', 'Banana', 'Cherry']
    if days is None:
        days = 30
    
    dates = [datetime.now() - timedelta(days=i) for i in range(days)]
    sales_data = {fruit: np.random.randint(sales_lower_bound, sales_upper_bound, days) for fruit in fruits}
    df = pd.DataFrame(sales_data, index=dates)
    
    # Create a seaborn boxplot of the sales
    boxplot = sns.boxplot(data=df)
    
    return df, boxplot