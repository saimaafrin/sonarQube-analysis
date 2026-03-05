import pandas as pd
import numpy as np
import random
from random import randint, seed
CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']
def task_func(mystrings, n_products, seed=0):
    # Generate random prices for each product
    prices = np.random.normal(50, 10, n_products)
    # Generate random categories for each product
    categories = np.random.choice(CATEGORIES, n_products)
    # Create a DataFrame with the product information
    df = pd.DataFrame({'Product Name': mystrings,
                       'Category': categories,
                       'Price': prices})
    # Replace spaces in product names with underscores
    df['Product Name'] = df['Product Name'].str.replace(' ', '_')
    return df
mystrings = ['Product 1', 'Product 2', 'Product 3']
n_products = len(mystrings)
seed = 0