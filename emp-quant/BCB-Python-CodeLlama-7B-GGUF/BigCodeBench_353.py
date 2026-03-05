
import pandas as pd
import random

def task_func(product_list, categories, min_value=10, max_value=100):
    # Generate random sales data for each product
    sales_data = []
    for product in product_list:
        category = random.choice(categories)
        quantity_sold = random.randint(min_value, max_value)
        revenue = random.randint(min_value, max_value)
        total_revenue = quantity_sold * revenue
        sales_data.append({
            'Product': product,
            'Category': category,
            'Quantity Sold': quantity_sold,
            'Revenue': revenue,
            'Total Revenue': total_revenue
        })

    # Create a pandas DataFrame with the sales data
    df = pd.DataFrame(sales_data)

    return df