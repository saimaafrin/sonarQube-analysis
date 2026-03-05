import pandas as pd
from random import randint, uniform, seed
def task_func(categories=None, months=None, random_seed=42):
    """
    Generates a DataFrame with simulated monthly sales data for various product categories.
    
    Parameters:
    - categories (list): A list of product categories.
    - months (list): A list of months.
    - random_seed (int): The seed for the random number generator to ensure reproducibility.
    
    Returns:
    - pandas.DataFrame: A DataFrame with three columns: 'Month', 'Category', and 'Sales'.
    
    Raises:
    - ValueError: If either 'categories' or 'months' is not provided as a list or if either is an empty list.
    """
    # Check if categories and months are provided as lists and are not empty
    if not categories or not months or not isinstance(categories, list) or not isinstance(months, list):
        raise ValueError("Both 'categories' and 'months' must be provided as non-empty lists.")
    
    # Set the random seed for reproducibility
    seed(random_seed)
    
    # Initialize an empty list to store the data
    data = []
    
    # Generate sales data for each category and month
    for month in months:
        for category in categories:
            # Generate a random sales value
            sales = randint(100, 500) + uniform(0, 1)
            # Append the data to the list
            data.append({'Month': month, 'Category': category, 'Sales': sales})
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    return df