import pandas as pd
import random
def task_func(product_list, categories, min_value = 10, max_value = 100):
    """
    Create a sales report for a list of products in different categories.
    The report includes the quantity sold and revenue generated for each product.
    """
    # Generate random sales data for each product
    sales_data = []
    for product in product_list:
        category = random.choice(categories)
        quantity_sold = random.randint(min_value, max_value)
        revenue = quantity_sold * random.randint(min_value, max_value)
        sales_data.append({
            'Product': product,
            'Category': category,
            'Quantity Sold': quantity_sold,
            'Revenue': revenue
        })

    # Create a pandas DataFrame with sales data
    df = pd.DataFrame(sales_data)

    # Sort the DataFrame by category and product
    df = df.sort_values(['Category', 'Product'])

    return df
product_list = ['Product A', 'Product B', 'Product C']
categories = ['Category 1', 'Category 2', 'Category 3']