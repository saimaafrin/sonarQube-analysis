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
        sales_data.append({
            'Product': product,
            'Category': random.choice(categories),
            'Quantity Sold': random.randint(min_value, max_value),
            'Revenue': random.randint(min_value, max_value) * random.randint(min_value, max_value),
            'Total Revenue': random.randint(min_value, max_value) * random.randint(min_value, max_value)
        })

    # Create a pandas DataFrame with sales data for the products
    df = pd.DataFrame(sales_data)

    # Calculate the total revenue for each category
    total_revenue = df.groupby('Category')['Total Revenue'].sum()

    # Calculate the average revenue for each category
    average_revenue = total_revenue / df.groupby('Category')['Quantity Sold'].sum()

    # Calculate the total quantity sold for each category
    total_quantity = df.groupby('Category')['Quantity Sold'].sum()

    # Calculate the average quantity sold for each category
    average_quantity = total_quantity / len(categories)

    # Create a new DataFrame with the calculated values
    result = pd.DataFrame({
        'Category': categories,
        'Total Revenue': total_revenue,
        'Average Revenue': average_revenue,
        'Total Quantity': total_quantity,
        'Average Quantity': average_quantity
    })

    return result
product_list = ['Product 1', 'Product 2', 'Product 3']
categories = ['Category 1', 'Category 2', 'Category 3']