
import pandas as pd
import numpy as np
import random
from random import randint, seed
# Constants
CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']
def task_func(mystrings, n_products, seed=0):
    # Create a list of product names
    product_names = ['Product_' + str(i) for i in range(n_products)]
    # Create a list of random prices
    prices = [randint(10, 100) for i in range(n_products)]
    # Create a list of random categories
    categories = [random.choice(CATEGORIES) for i in range(n_products)]
    # Create a DataFrame with the product information
    df = pd.DataFrame({
        'Product Name': product_names,
        'Category': categories,
        'Price': prices
    })
    return df