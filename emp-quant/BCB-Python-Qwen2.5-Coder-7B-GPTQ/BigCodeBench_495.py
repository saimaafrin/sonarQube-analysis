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
    np.random.seed(random_seed)
    dates = pd.date_range(start='2023-01-01', periods=days)
    data = {
        'Groceries': np.random.randint(0, 101, days),
        'Entertainment': np.random.randint(0, 101, days),
        'Rent': np.random.randint(0, 101, days),
        'Utilities': np.random.randint(0, 101, days),
        'Miscellaneous': np.random.randint(0, 101, days)
    }
    df = pd.DataFrame(data, index=dates)
    return df
days = 5