from random import randint
from statistics import mean
import pandas as pd
def task_func(products_list):
    """
    This function takes in a list of product names and generates random sales data for each product over a period of
    12 months. It then calculates the average sales for each product and returns the results as a pandas DataFrame with
    columns: 'Product', 'Month 1', 'Month 2', ..., 'Month 12', 'Average Sales'..
    
    Parameters:
    products_list (list): A list of product names.
    
    Returns:
    DataFrame: A pandas DataFrame with columns: 'Product', 'Month 1', 'Month 2', ..., 'Month 12', 'Average Sales'.
    
    Requirements:
    - pandas
    - random
    - statistics
    
    Example:
    >>> products = ['Apples', 'Bananas', 'Grapes', 'Oranges', 'Pineapples']
    >>> sales_data = task_func(products)
    >>> type(sales_data)
    <class 'pandas.core.frame.DataFrame'>
    """
    # Create a list of months
    months = ['Month ' + str(i) for i in range(1, 13)]

    # Create a list of random sales data for each product
    sales_data = []
    for product in products_list:
        sales = []
        for month in months:
            sales.append(randint(100, 1000))
        sales_data.append([product] + sales)

    # Create a DataFrame with the sales data
    df = pd.DataFrame(sales_data, columns=['Product'] + months)

    # Calculate the average sales for each product
    average_sales = []
    for product in products_list:
        average_sales.append(mean(df[df['Product'] == product][months]))

    # Add the average sales to the DataFrame
    df['Average Sales'] = average_sales

    return df