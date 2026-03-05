import pandas as pd
from random import choices, seed
def task_func(products, ratings, weights, random_seed=42):
    """
    Generates a DataFrame containing ratings for a given list of products.
    Ratings are generated randomly based on the provided weights.
    The DataFrame is sorted by ratings in descending order.

    Parameters
    ----------
    products : list
        A list of products.
    ratings : list
        A list of ratings for each product.
    weights : list
        A list of weights for each product.
    random_seed : int, optional
        A random seed for reproducibility.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with two columns: 'Product' and 'Rating', sorted by 'Rating' in descending order.
    """
    # Set random seed for reproducibility
    seed(random_seed)

    # Generate ratings for each product
    ratings = [choices(ratings, weights=weights) for _ in range(len(products))]

    # Create DataFrame with product and rating columns
    df = pd.DataFrame({'Product': products, 'Rating': ratings})

    # Sort DataFrame by rating in descending order
    df.sort_values(by='Rating', ascending=False, inplace=True)

    return df
products = ['Product 1', 'Product 2', 'Product 3']
ratings = [1, 2, 3]
weights = [0.5, 0.3, 0.2]