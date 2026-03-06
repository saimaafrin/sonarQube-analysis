import pandas as pd
import random
CATEGORIES = ['A', 'B', 'C', 'D', 'E']
def task_func(value_range=(0, 100)):
    """
    Generate a category distribution within a specified range and return as a DataFrame.

    Parameters:
    value_range (tuple): A tuple specifying the range (min, max) for generating random values for categories.
    
    Returns:
    DataFrame: A pandas DataFrame that has two columns: 'Category' (category names) and 'Count' (count of each category). 

    Requirements:
    - pandas
    - random

    Example:
    >>> random.seed(0)
    >>> df = task_func()
    >>> df['Count'][0] >= 0
    True
    """
    # Generate random values for categories
    values = [random.randint(value_range[0], value_range[1]) for _ in range(len(CATEGORIES))]

    # Create a DataFrame with two columns: 'Category' and 'Count'
    df = pd.DataFrame({'Category': CATEGORIES, 'Count': values})

    # Return the DataFrame
    return df