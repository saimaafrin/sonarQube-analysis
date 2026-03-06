
import pandas as pd
from random import choices, seed

def task_func(products, ratings, weights, random_seed=42):
    """
    Generates a DataFrame containing ratings for a given list of products.
    
    Parameters:
    - products (list): A list of product names.
    - ratings (list): A list of possible rating values.
    - weights (list): A list of weights corresponding to each rating value.
    - random_seed (int): Seed for the random number generator for reproducibility.
    
    Returns:
    - pandas.DataFrame: A DataFrame with two columns: 'Product' and 'Rating', sorted by 'Rating' in descending order.
    """
    # Set the random seed for reproducibility
    seed(random_seed)
    
    # Generate random ratings for each product
    ratings_list = choices(ratings, weights, k=len(products))
    
    # Create a DataFrame
    df = pd.DataFrame({'Product': products, 'Rating': ratings_list})
    
    # Sort the DataFrame by Rating in descending order
    df_sorted = df.sort_values(by='Rating', ascending=False)
    
    return df_sorted