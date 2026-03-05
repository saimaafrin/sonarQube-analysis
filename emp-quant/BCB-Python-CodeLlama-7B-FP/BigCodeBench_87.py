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
        List of products to generate ratings for.
    ratings : list
        List of ratings for each product.
    weights : list
        List of weights for each product.
    random_seed : int, optional
        Random seed for reproducibility.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with two columns: 'Product' and 'Rating', sorted by 'Rating' in descending order.
    """
    seed(random_seed)
    ratings = [random.choices(ratings, weights=weights) for _ in range(len(products))]
    df = pd.DataFrame({'Product': products, 'Rating': ratings})
    return df.sort_values(by='Rating', ascending=False)
products = ['Product 1', 'Product 2', 'Product 3']
ratings = [1, 2, 3]
weights = [0.5, 0.3, 0.2]