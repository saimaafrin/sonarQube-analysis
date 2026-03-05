
from random import randint
from statistics import mean
import pandas as pd

def task_func(products_list):
    # Initialize a dictionary to store sales data
    sales_data = {}
    
    # Generate random sales data for each product over 12 months
    for product in products_list:
        sales_data[product] = [randint(1, 100) for _ in range(12)]
    
    # Create a DataFrame from the sales data
    df = pd.DataFrame(sales_data)
    
    # Calculate the average sales for each product
    df['Average Sales'] = df.mean(axis=1)
    
    # Return the DataFrame
    return df