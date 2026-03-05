
import pandas as pd
import random

def task_func(product_list, categories):
    products = []
    for product in product_list:
        product_data = {
            'Product': product,
            'Category': random.choice(categories),
            'Quantity Sold': random.randint(1, 100),
            'Revenue': random.randint(10, 100) * random.randint(1, 100)
        }
        products.append(product_data)
    return pd.DataFrame(products)