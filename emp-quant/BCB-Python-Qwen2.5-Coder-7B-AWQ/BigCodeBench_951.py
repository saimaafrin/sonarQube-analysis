import pandas as pd
import numpy as np
import random
from random import randint, seed
CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']
def task_func(mystrings, n_products, seed=0):
    # Initialize the seed for reproducibility
    seed(seed)
    
    # Create an empty list to store product data
    products = []
    
    # Generate product data
    for _ in range(n_products):
        product_name = mystrings[randint(0, len(mystrings) - 1)].replace(' ', '_')
        category = random.choice(CATEGORIES)
        price = np.random.normal(50, 10)
        
        # Append the product data as a tuple to the list
        products.append((product_name, category, price))
    
    # Create a DataFrame from the list of products
    df = pd.DataFrame(products, columns=['Product Name', 'Category', 'Price'])
    
    return df