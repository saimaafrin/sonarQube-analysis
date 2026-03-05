import pandas as pd
import numpy as np
def task_func(days, random_seed=0):
    """
    Generates a spending report DataFrame for the given number of days.

    Parameters:
    days (int): The number of days to generate data for.
    random_seed (int): The seed for the random number generator for reproducibility.

    Returns:
    pd.DataFrame: A DataFrame containing spending details for specified days.
    """
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Define the column names
    columns = ['Groceries', 'Entertainment', 'Rent', 'Utilities', 'Miscellaneous']
    
    # Create a date range starting from '2023-01-01'
    date_range = pd.date_range(start='2023-01-01', periods=days)
    
    # Generate random spending data for each category
    data = {col: np.random.randint(0, 101, size=days) for col in columns}
    
    # Create the DataFrame
    df = pd.DataFrame(data, index=date_range)
    
    return df