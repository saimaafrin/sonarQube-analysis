import pandas as pd
import random
def task_func(product_list, categories):
    # Create a list of random quantities sold for each product
    quantities = [random.randint(1, 100) for _ in range(len(product_list))]

    # Create a list of random revenue for each product
    revenue = [quantity * random.randint(10, 100) for quantity in quantities]

    # Create a dictionary with product names as keys and lists of quantities and revenue as values
    data = {product: [quantity, revenue] for product, quantity, revenue in zip(product_list, quantities, revenue)}

    # Create a pandas DataFrame with the sales data
    df = pd.DataFrame(data, columns=['Product', 'Category', 'Quantity Sold', 'Revenue'])

    return df
product_list = ['Product A', 'Product B', 'Product C']
categories = ['Category 1', 'Category 2', 'Category 3']