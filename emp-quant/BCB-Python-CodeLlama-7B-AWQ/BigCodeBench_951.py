import pandas as pd
import numpy as np
import random
from random import randint, seed
CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']
def task_func(mystrings, n_products, seed=0):
    """
    Create a product catalog DataFrame where each row represents a product with the following columns:
    - 'Product Name': The name of the product with spaces replaced by underscores.
    - 'Category': The category to which the product belongs.
    - 'Price': The price of the product, generated randomly based on a normal distribution with a mean of 50 and a standard deviation of 10.
    """
    # Set random seed for reproducibility
    seed = seed
    # Create a list of product names
    product_names = []
    for i in range(n_products):
        product_names.append('Product ' + str(i + 1))
    # Create a list of product categories
    product_categories = []
    for i in range(n_products):
        product_categories.append(CATEGORIES[randint(0, len(CATEGORIES) - 1)])
    # Create a list of product prices
    product_prices = []
    for i in range(n_products):
        product_prices.append(np.random.normal(50, 10))
    # Create a DataFrame with the product catalog information
    product_catalog = pd.DataFrame({'Product Name': product_names,
                                    'Category': product_categories,
                                    'Price': product_prices})
    return product_catalog
mystrings = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']
n_products = 5
seed = 0