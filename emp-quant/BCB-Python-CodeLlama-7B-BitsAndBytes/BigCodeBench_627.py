
from random import randint
from statistics import mean
import pandas as pd

def task_func(products_list):
    # Create a dictionary to store the sales data for each product
    sales_data = {}

    # Loop through the list of products
    for product in products_list:
        # Generate random sales data for each product over a period of 12 months
        sales_data[product] = [randint(100, 1000) for _ in range(12)]

    # Calculate the average sales for each product
    average_sales = [mean(sales_data[product]) for product in products_list]

    # Create a pandas DataFrame with the results
    df = pd.DataFrame({'Product': products_list, 'Average Sales': average_sales})

    # Add columns for each month's sales data
    for i in range(1, 13):
        df['Month {}'.format(i)] = sales_data[product][i-1]

    return df