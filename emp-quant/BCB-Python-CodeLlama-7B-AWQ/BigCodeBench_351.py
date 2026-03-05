import pandas as pd
import random
def task_func(product_list, categories, min_value = 10, max_value = 100):
    """
    Create a sales report for a list of products in different categories.
    The report includes the quantity sold and revenue generated for each product.
    """
    # Create a list of random quantities sold for each product
    quantities = [random.randint(min_value, max_value) for _ in range(len(product_list))]

    # Create a list of random revenue generated for each product
    revenue = [random.randint(min_value, max_value) * quantity for quantity in quantities]

    # Create a DataFrame with the sales data
    sales_data = pd.DataFrame({
        'Product': product_list,
        'Category': categories,
        'Quantity Sold': quantities,
        'Revenue': revenue
    })

    return sales_data
product_list = ['Product A', 'Product B', 'Product C']
categories = ['Category 1', 'Category 2', 'Category 3']