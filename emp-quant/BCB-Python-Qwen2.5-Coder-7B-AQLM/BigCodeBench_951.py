
import pandas as pd
import numpy as np
import random
from random import randint, seed
# Constants
CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']

def task_func(mystrings, n_products, seed=0):
    seed(seed)
    product_catalog = []
    for _ in range(n_products):
        product_name = mystrings[randint(0, len(mystrings) - 1)].replace(' ', '_')
        category = random.choice(CATEGORIES)
        price = np.random.normal(50, 10)
        product_catalog.append({'Product Name': product_name, 'Category': category, 'Price': price})
    return pd.DataFrame(product_catalog)