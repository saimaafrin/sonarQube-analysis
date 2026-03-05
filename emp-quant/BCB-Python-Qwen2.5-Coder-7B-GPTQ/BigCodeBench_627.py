from random import randint
from statistics import mean
import pandas as pd
def task_func(products_list):
    # Initialize an empty list to store the data
    data = []
    
    # Loop through each product in the products_list
    for product in products_list:
        # Generate random sales data for each month
        sales_data = [randint(100, 1000) for _ in range(12)]
        
        # Calculate the average sales
        average_sales = mean(sales_data)
        
        # Append the product and its sales data to the data list
        data.append([product] + sales_data + [average_sales])
    
    # Create a pandas DataFrame from the data list
    df = pd.DataFrame(data, columns=['Product', 'Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6', 'Month 7', 'Month 8', 'Month 9', 'Month 10', 'Month 11', 'Month 12', 'Average Sales'])
    
    # Return the DataFrame
    return df