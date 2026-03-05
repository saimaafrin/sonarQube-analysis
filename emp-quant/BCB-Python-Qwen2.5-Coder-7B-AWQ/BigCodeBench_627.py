from random import randint
from statistics import mean
import pandas as pd
def task_func(products_list):
    # Initialize a list to store the sales data for each product
    sales_data = []
    
    # Loop through each product in the products_list
    for product in products_list:
        # Generate random sales data for each month
        monthly_sales = [randint(100, 1000) for _ in range(12)]
        
        # Calculate the average sales for the product
        average_sales = mean(monthly_sales)
        
        # Append the product name and its sales data to the sales_data list
        sales_data.append([product] + monthly_sales + [average_sales])
    
    # Create a pandas DataFrame from the sales_data list
    df = pd.DataFrame(sales_data, columns=['Product', 'Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6', 'Month 7', 'Month 8', 'Month 9', 'Month 10', 'Month 11', 'Month 12', 'Average Sales'])
    
    # Return the DataFrame
    return df