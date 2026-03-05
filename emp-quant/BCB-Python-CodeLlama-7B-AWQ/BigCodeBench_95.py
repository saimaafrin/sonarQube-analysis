import pandas as pd
from random import randint, uniform, seed
def task_func(categories=None, months=None, random_seed=42):
    """
    Generates a DataFrame with simulated monthly sales data for various product categories, ensuring reproducibility through the use of a random seed.

    Parameters
    ----------
    categories : list of str
        List of product categories to generate sales data for.
    months : list of int
        List of months to generate sales data for.
    random_seed : int
        Random seed to use for generating sales data.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with three columns: 'Month', 'Category', and 'Sales'.

    Raises
    ------
    ValueError
        If either 'categories' or 'months' is not provided as a list or if either is an empty list.
    """
    if not isinstance(categories, list) or not categories:
        raise ValueError("'categories' must be a non-empty list of strings")
    if not isinstance(months, list) or not months:
        raise ValueError("'months' must be a non-empty list of integers")

    # Set the random seed
    seed(random_seed)

    # Generate sales data for each category and month
    sales_data = []
    for category in categories:
        for month in months:
            sales_data.append({
                'Month': month,
                'Category': category,
                'Sales': randint(100, 500) + uniform(0, 1)
            })

    # Create a DataFrame from the sales data
    df = pd.DataFrame(sales_data, columns=['Month', 'Category', 'Sales'])

    return df
categories = ['A', 'B', 'C']
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]