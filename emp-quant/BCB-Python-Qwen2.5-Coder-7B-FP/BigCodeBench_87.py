import pandas as pd
from random import choices, seed
def task_func(products, ratings, weights, random_seed=42):
    """
    Generates a DataFrame containing ratings for a given list of products.
    Ratings are generated randomly based on the provided weights.
    The DataFrame is sorted by ratings in descending order.
    
    Parameters:
    - products (list): A list of product names.
    - ratings (list): A list of possible ratings for each product.
    - weights (list): A list of weights corresponding to each rating.
    - random_seed (int): Seed for the random number generator for reproducibility.
    
    Returns:
    - pandas.DataFrame: A DataFrame with two columns: 'Product' and 'Rating', sorted by 'Rating' in descending order.
    """
    seed(random_seed)
    ratings_list = choices(ratings, weights, k=len(products))
    df = pd.DataFrame({'Product': products, 'Rating': ratings_list})
    df = df.sort_values(by='Rating', ascending=False)
    return df
products = ['Product A', 'Product B', 'Product C']
ratings = [1, 2, 3, 4, 5]
weights = [0.1, 0.2, 0.3, 0.3, 0.1]