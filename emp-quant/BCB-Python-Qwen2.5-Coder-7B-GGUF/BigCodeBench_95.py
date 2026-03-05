
import pandas as pd
from random import randint, uniform, seed

def task_func(categories=None, months=None, random_seed=42):
    if categories is None or not isinstance(categories, list) or not categories:
        raise ValueError("The 'categories' parameter must be a non-empty list.")
    if months is None or not isinstance(months, list) or not months:
        raise ValueError("The 'months' parameter must be a non-empty list.")
    
    seed(random_seed)
    data = []
    for month in months:
        for category in categories:
            sales = randint(100, 500) + uniform(0, 1)
            data.append({'Month': month, 'Category': category, 'Sales': sales})
    
    return pd.DataFrame(data)