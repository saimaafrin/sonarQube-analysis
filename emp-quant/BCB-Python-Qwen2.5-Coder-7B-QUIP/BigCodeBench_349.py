
import pandas as pd
import random

def task_func(product_list, categories):
    # Initialize an empty list to store the sales data
    sales_data = []
    
    # Iterate over each product in the product list
    for product in product_list:
        # Get a random category for the product
        category = random.choice(categories)
        
        # Get a random quantity sold between 1 and 100
        quantity_sold = random.randint(1, 100)
        
        # Get a random revenue between 10 and 100
        revenue = quantity_sold * random.randint(10, 100)
        
        # Append the data to the sales_data list
        sales_data.append({
            'Product': product,
            'Category': category,
            'Quantity Sold': quantity_sold,
            'Revenue': revenue
        })
    
    # Create a DataFrame from the sales_data list
    sales_df = pd.DataFrame(sales_data)
    
    # Return the DataFrame
    return sales_df