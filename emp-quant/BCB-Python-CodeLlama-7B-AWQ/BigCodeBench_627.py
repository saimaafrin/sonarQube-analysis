from random import randint
from statistics import mean
import pandas as pd
def task_func(products_list):
    """
    Generates random sales data for each product over a period of 12 months and calculates the average sales for each product.
    Returns a pandas DataFrame with columns: 'Product', 'Month 1', 'Month 2', ..., 'Month 12', 'Average Sales'.
    """
    # Create a list of random sales data for each product
    sales_data = []
    for product in products_list:
        sales = [randint(100, 1000) for _ in range(12)]
        sales_data.append({'Product': product, 'Sales': sales})

    # Create a pandas DataFrame from the sales data
    df = pd.DataFrame(sales_data)

    # Calculate the average sales for each product
    df['Average Sales'] = df.groupby('Product')['Sales'].transform('mean')

    return df
products_list = ['Product 1', 'Product 2', 'Product 3']