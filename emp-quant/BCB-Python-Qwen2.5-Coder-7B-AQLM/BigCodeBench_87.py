
import pandas as pd
from random import choices, seed

def task_func(products, ratings, weights, random_seed=42):
    seed(random_seed)
    ratings_list = choices(ratings, weights, k=len(products))
    df = pd.DataFrame({'Product': products, 'Rating': ratings_list})
    df = df.sort_values(by='Rating', ascending=False)
    return df