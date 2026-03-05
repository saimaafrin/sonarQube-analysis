
import pandas as pd
from random import choices, seed

def task_func(products, ratings, weights, random_seed=42):
    seed(random_seed)
    ratings_list = []
    for product in products:
        ratings_list.append({'Product': product, 'Rating': choices(ratings, weights=weights)})
    ratings_df = pd.DataFrame(ratings_list)
    ratings_df = ratings_df.sort_values(by='Rating', ascending=False)
    return ratings_df

ratings_df = task_func(products, ratings, weights, random_seed)
print(ratings_df)