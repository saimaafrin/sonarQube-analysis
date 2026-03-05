from random import randint
from statistics import mean
import pandas as pd
def task_func(products_list):
    # Initialize a dictionary to store sales data
    sales_data = {}
    
    # Generate random sales data for each product over 12 months
    for product in products_list:
        sales_data[product] = [randint(10, 100) for _ in range(12)]
    
    # Calculate the average sales for each product
    for product in sales_data:
        sales_data[product].append(mean(sales_data[product]))
    
    # Create a pandas DataFrame from the sales data
    df = pd.DataFrame(sales_data)
    
    # Reorder columns to match the required format
    columns = ['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales']
    df = df[columns]
    
    # Set the product names as the index
    df.set_index('Product', inplace=True)
    
    return df