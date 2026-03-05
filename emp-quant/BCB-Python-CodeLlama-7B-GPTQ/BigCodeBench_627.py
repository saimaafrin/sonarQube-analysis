from random import randint
from statistics import mean
import pandas as pd
def task_func(products_list):
    """
    This function takes in a list of product names and generates random sales data for each product over a period of 12 months. It then calculates the average sales for each product and returns the results as a pandas DataFrame with columns: 'Product', 'Month 1', 'Month 2', ..., 'Month 12', 'Average Sales'.
    """
    # Generate random sales data for each product
    sales_data = {}
    for product in products_list:
        sales_data[product] = [randint(100, 1000) for _ in range(12)]

    # Calculate average sales for each product
    average_sales = {}
    for product, sales in sales_data.items():
        average_sales[product] = mean(sales)

    # Create a pandas DataFrame with the results
    df = pd.DataFrame(average_sales, index=['Average Sales'])
    df.columns = ['Product', 'Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6', 'Month 7', 'Month 8', 'Month 9', 'Month 10', 'Month 11', 'Month 12']

    return df
products_list = ['Product 1', 'Product 2', 'Product 3']