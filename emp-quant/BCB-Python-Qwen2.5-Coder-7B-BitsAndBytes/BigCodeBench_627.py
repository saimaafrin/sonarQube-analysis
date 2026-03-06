
from random import randint
from statistics import mean
import pandas as pd

def task_func(products_list):
    # Initialize an empty list to store the sales data
    sales_data = []
    
    # Loop through each product in the products_list
    for product in products_list:
        # Generate random sales data for each month (12 months)
        monthly_sales = [randint(100, 500) for _ in range(12)]
        
        # Calculate the average sales
        average_sales = mean(monthly_sales)
        
        # Append the product name and its sales data to the sales_data list
        sales_data.append([product] + monthly_sales + [average_sales])
    
    # Create a pandas DataFrame from the sales_data list
    df = pd.DataFrame(sales_data, columns=['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales'])
    
    return df