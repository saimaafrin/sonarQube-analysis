import pandas as pd
import random
def task_func(product_list, categories):
    # Initialize an empty list to store the sales data
    sales_data = []
    
    # Loop through each product and category
    for product in product_list:
        for category in categories:
            # Generate random quantity sold and revenue
            quantity_sold = random.randint(1, 100)
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
    
    return sales_df