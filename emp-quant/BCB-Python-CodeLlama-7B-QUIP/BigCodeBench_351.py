
import pandas as pd
import random

def task_func(product_list, categories, min_value = 10, max_value = 100):
    # Generate some random data for the products
    for product in product_list:
        product_data = {
            'Product': product,
            'Category': random.choice(categories),
            'Quantity Sold': random.randint(min_value, max_value),
            'Revenue': random.randint(min_value, max_value)
        }
        data.append(product_data)

    # Create a pandas DataFrame with the data
    df = pd.DataFrame(data)

    return df

df = task_func(product_list, categories)

print(df)