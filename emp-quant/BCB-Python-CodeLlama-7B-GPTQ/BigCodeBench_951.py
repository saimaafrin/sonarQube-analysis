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
    # Generate random product names
    product_names = [f"Product {i+1}" for i in range(n_products)]
    # Generate random categories
    categories = [random.choice(CATEGORIES) for _ in range(n_products)]
    # Generate random prices
    prices = [np.random.normal(50, 10) for _ in range(n_products)]
    # Create DataFrame
    df = pd.DataFrame({
        "Product Name": product_names,
        "Category": categories,
        "Price": prices
    })
    return df