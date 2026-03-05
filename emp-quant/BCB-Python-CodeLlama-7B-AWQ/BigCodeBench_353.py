import pandas as pd
import random
def task_func(product_list, categories, min_value = 10, max_value = 100):
    """
    Create a sales report for a list of products in different categories.
    The report includes the quantity sold, revenue for 1 product, and total revenue generated for each product.
    """
    # Generate random sales data for each product
    sales_data = []
    for product in product_list:
        quantity_sold = random.randint(min_value, max_value)
        revenue = random.randint(min_value, max_value) * quantity_sold
        total_revenue = revenue
        sales_data.append({
            'Product': product,
            'Category': categories[product],
            'Quantity Sold': quantity_sold,
            'Revenue': revenue,
            'Total Revenue': total_revenue
        })

    # Create a pandas DataFrame with sales data
    sales_df = pd.DataFrame(sales_data)

    # Sort the DataFrame by total revenue
    sales_df = sales_df.sort_values(by='Total Revenue', ascending=False)

    return sales_df
product_list = ['Product A', 'Product B', 'Product C']
categories = {'Product A': 'Category A', 'Product B': 'Category B', 'Product C': 'Category C'}
min_value = 10
max_value = 100