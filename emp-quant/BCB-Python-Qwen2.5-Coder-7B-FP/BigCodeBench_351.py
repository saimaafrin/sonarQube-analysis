import pandas as pd
import random
def task_func(product_list, categories, min_value=10, max_value=100):
    # Initialize an empty list to store the sales data
    sales_data = []
    
    # Loop through each product and category to generate sales data
    for product in product_list:
        for category in categories:
            # Generate random quantity sold and revenue
            quantity_sold = random.randint(min_value, max_value)
            revenue = random.randint(min_value, max_value) * quantity_sold
            
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
product_list = ['Laptop', 'Smartphone', 'Tablet']
categories = ['Electronics', 'Gadgets', 'Accessories']