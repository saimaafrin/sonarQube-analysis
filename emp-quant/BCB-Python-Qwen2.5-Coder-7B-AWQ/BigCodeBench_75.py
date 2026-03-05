import pandas as pd
import numpy as np
import itertools
from datetime import datetime, timedelta
import seaborn as sns
def task_func(df, fruits=None, days=None, seed=None, sales_lower_bound=1, sales_upper_bound=50):
    """
    Appends randomly generated sales data for specified fruits over a given range of days to a DataFrame,
    and returns a seaborn boxplot of the sales.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - fruits (list): List of fruits to generate sales data for. If None, generates sales for all fruits in the DataFrame.
    - days (int): Number of days to generate sales data for. If None, generates sales for all days in the DataFrame.
    - seed (int): Seed for the random number generator for reproducibility.
    - sales_lower_bound (int): Lower bound for the sales data.
    - sales_upper_bound (int): Upper bound for the sales data.
    
    Returns:
    - Tuple[pd.DataFrame, sns.axisgrid.FacetGrid]: Updated DataFrame with sales data and a seaborn boxplot of the sales.
    """
    # Check if df is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    
    # Check if df is empty
    if df.empty:
        raise ValueError("df cannot be empty")
    
    # Check if sales_lower_bound is less than sales_upper_bound
    if sales_lower_bound >= sales_upper_bound:
        raise ValueError("sales_lower_bound must be less than sales_upper_bound")
    
    # Set the seed for reproducibility
    if seed is not None:
        np.random.seed(seed)
    
    # Get the list of fruits from the DataFrame if fruits is None
    if fruits is None:
        fruits = df['fruit'].unique()
    
    # Get the list of dates from the DataFrame if days is None
    if days is None:
        start_date = df['date'].min()
        end_date = df['date'].max()
        days = (end_date - start_date).days + 1
    
    # Generate random sales data
    sales_data = []
    for fruit in fruits:
        for day in range(days):
            sales = np.random.randint(sales_lower_bound, sales_upper_bound)
            sales_data.append({'date': start_date + timedelta(days=day), 'fruit': fruit, 'sales': sales})
    
    # Convert the sales data to a DataFrame
    sales_df = pd.DataFrame(sales_data)
    
    # Append the sales data to the input DataFrame
    df = pd.concat([df, sales_df], ignore_index=True)
    
    # Create a seaborn boxplot of the sales
    boxplot = sns.boxplot(x='fruit', y='sales', data=df)
    
    return df, boxplot