
import pandas as pd
from random import choices, seed

def task_func(products, ratings, weights, random_seed=42):
    seed(random_seed)
    ratings = [choices(ratings, weights=weights)]
    return pd.DataFrame({'Product': products, 'Rating': ratings})