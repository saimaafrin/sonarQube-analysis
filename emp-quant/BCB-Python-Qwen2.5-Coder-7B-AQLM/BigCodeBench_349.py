
import pandas as pd
import random

def task_func(product_list, categories):
    data = []
    for product in product_list:
        category = random.choice(categories)
        quantity_sold = random.randint(1, 100)
        revenue = quantity_sold * random.randint(10, 100)
        data.append({'Product': product, 'Category': category, 'Quantity Sold': quantity_sold, 'Revenue': revenue})
    
    df = pd.DataFrame(data)
    return df