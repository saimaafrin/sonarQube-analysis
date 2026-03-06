
import pandas as pd
from random import randint, uniform, seed

def task_func(categories=None, months=None, random_seed=42):
    # Check if categories and months are provided and are lists
    if not (isinstance(categories, list) and isinstance(months, list)):
        raise ValueError("Both 'categories' and 'months' must be provided as lists.")
    
    # Check if categories and months are not empty
    if not categories or not months:
        raise ValueError("Both 'categories' and 'months' must contain at least one element.")
    
    # Set the random seed for reproducibility
    seed(random_seed)
    
    # Initialize an empty list to store the data
    data = []
    
    # Generate sales data for each category and month
    for month in months:
        for category in categories:
            # Calculate a random sales value within the specified range
            sales_value = randint(100, 500) + uniform(0, 1)
            # Append the data to the list
            data.append([month, category, sales_value])
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['Month', 'Category', 'Sales'])
    
    return df