
import pandas as pd
import numpy as np
import random
from random import randint, seed
# Constants
CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']
def task_func(mystrings, n_products, seed=0):
    # Generate random prices for each product
    prices = np.random.normal(50, 10, n_products)
    # Create a list of product names
    product_names = []
    for i in range(n_products):
        product_name = mystrings[i].replace(' ', '_')
        product_names.append(product_name)
    # Create a list of categories for each product
    categories = []
    for i in range(n_products):
        category = random.choice(CATEGORIES)
        categories.append(category)
    # Create a DataFrame with the product catalog information
    product_catalog = pd.DataFrame({'Product Name': product_names, 'Category': categories, 'Price': prices})
    return product_catalog