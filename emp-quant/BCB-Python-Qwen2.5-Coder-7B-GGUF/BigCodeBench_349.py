
import pandas as pd
import random

def task_func(product_list, categories):
    data = {
        'Product': product_list,
        'Category': [random.choice(categories) for _ in product_list],
        'Quantity Sold': [random.randint(1, 100) for _ in product_list],
        'Revenue': [q * random.randint(10, 100) for q in data['Quantity Sold']]
    }
    return pd.DataFrame(data)