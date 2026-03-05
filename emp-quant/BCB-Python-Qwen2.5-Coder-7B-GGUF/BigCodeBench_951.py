
import pandas as pd
import numpy as np
import random
from random import randint, seed
# Constants
CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']

def task_func(mystrings, n_products, seed=0):
    seed(seed)  # Set the seed for reproducibility
    product_catalog = []
    
    for _ in range(n_products):
        product_name = random.choice(mystrings).replace(" ", "_")
        category = random.choice(CATEGORIES)
        price = np.random.normal(50, 10)
        product_catalog.append([product_name, category, price])
    
    df = pd.DataFrame(product_catalog, columns=['Product Name', 'Category', 'Price'])
    return df