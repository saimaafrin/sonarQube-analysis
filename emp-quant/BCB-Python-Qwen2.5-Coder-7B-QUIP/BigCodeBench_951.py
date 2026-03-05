
import pandas as pd
import numpy as np
import random
from random import randint, seed
# Constants
CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']

def task_func(mystrings, n_products, seed=0):
    # Seed the random generator
    seed(seed)
    
    # Initialize an empty list to store product data
    product_data = []
    
    # Generate n_products rows
    for _ in range(n_products):
        # Generate a random category
        category = random.choice(CATEGORIES)
        
        # Generate a random product name with spaces replaced by underscores
        product_name = mystrings[randint(0, len(mystrings) - 1)].replace(' ', '_')
        
        # Generate a random price from a normal distribution with mean 50 and std dev 10
        price = np.random.normal(50, 10)
        
        # Append the product data to the list
        product_data.append({
            'Product Name': product_name,
            'Category': category,
            'Price': price
        })
    
    # Create a DataFrame from the product data
    product_catalog = pd.DataFrame(product_data)
    
    return product_catalog