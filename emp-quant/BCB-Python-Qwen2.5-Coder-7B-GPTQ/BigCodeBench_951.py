import pandas as pd
import numpy as np
import random
from random import randint, seed
CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']
def task_func(mystrings, n_products, seed=0):
    # Set the seed for reproducibility
    random.seed(seed)
    
    # Initialize an empty list to store product data
    products = []
    
    # Loop to generate each product
    for _ in range(n_products):
        # Randomly select a category
        category = random.choice(CATEGORIES)
        
        # Generate a random price based on a normal distribution
        price = np.random.normal(50, 10)
        
        # Replace spaces in the product name with underscores
        product_name = mystrings.replace(' ', '_')
        
        # Append the product data to the list
        products.append([product_name, category, price])
    
    # Create a DataFrame from the list of products
    product_catalog = pd.DataFrame(products, columns=['Product Name', 'Category', 'Price'])
    
    return product_catalog