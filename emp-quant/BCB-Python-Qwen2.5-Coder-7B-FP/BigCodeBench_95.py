import pandas as pd
from random import randint, uniform, seed
def task_func(categories=None, months=None, random_seed=42):
    # Check if categories and months are provided as lists and are not empty
    if not isinstance(categories, list) or not isinstance(months, list) or not categories or not months:
        raise ValueError("Both 'categories' and 'months' must be provided as non-empty lists.")
    
    # Set the random seed for reproducibility
    seed(random_seed)
    
    # Initialize an empty list to store the sales data
    sales_data = []
    
    # Generate sales data for each category and month
    for month in months:
        for category in categories:
            # Generate a random sales value using the specified formula
            sales_value = randint(100, 500) + uniform(0, 1)
            # Append the data to the list
            sales_data.append({'Month': month, 'Category': category, 'Sales': sales_value})
    
    # Create a DataFrame from the sales data
    df = pd.DataFrame(sales_data)
    
    return df