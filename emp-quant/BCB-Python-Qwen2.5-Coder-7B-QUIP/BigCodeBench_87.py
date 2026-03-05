
import pandas as pd
from random import choices, seed

def task_func(products, ratings, weights, random_seed=42):
    # Set the random seed for reproducibility
    seed(random_seed)
    
    # Generate random ratings for each product based on the provided weights
    ratings_list = choices(ratings, weights, k=len(products))
    
    # Create a DataFrame with 'Product' and 'Rating' columns
    df = pd.DataFrame({'Product': products, 'Rating': ratings_list})
    
    # Sort the DataFrame by 'Rating' in descending order
    df = df.sort_values(by='Rating', ascending=False)
    
    return df