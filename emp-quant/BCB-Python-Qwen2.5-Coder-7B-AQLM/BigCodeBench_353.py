
import pandas as pd
import random

def task_func(product_list, categories, min_value=10, max_value=100):
    data = []
    for product in product_list:
        category = random.choice(categories)
        quantity_sold = random.randint(min_value, max_value)
        revenue = random.randint(min_value, max_value)
        total_revenue = quantity_sold * revenue
        data.append({
            'Product': product,
            'Category': category,
            'Quantity Sold': quantity_sold,
            'Revenue': revenue,
            'Total Revenue': total_revenue
        })
    df = pd.DataFrame(data)
    return df