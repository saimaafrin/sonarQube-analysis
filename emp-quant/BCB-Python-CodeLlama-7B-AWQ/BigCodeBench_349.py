import pandas as pd
import random
def task_func(product_list, categories):
    """
    Create a sales report for a list of products in different categories.
    The report includes the quantity sold and revenue generated for each product.
    """
    # Create a list of random quantities for each product
    quantities = [random.randint(1, 100) for _ in range(len(product_list))]

    # Create a list of random revenues for each product
    revenues = [quantity * random.randint(10, 100) for quantity in quantities]

    # Create a DataFrame with the sales data
    sales_data = pd.DataFrame({
        'Product': product_list,
        'Category': categories,
        'Quantity Sold': quantities,
        'Revenue': revenues
    })

    return sales_data
product_list = ['Product A', 'Product B', 'Product C']
categories = ['Category 1', 'Category 2', 'Category 3']