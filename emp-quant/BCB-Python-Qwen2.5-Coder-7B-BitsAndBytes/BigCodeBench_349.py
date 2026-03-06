
import pandas as pd
import random

def task_func(product_list, categories):
    # Initialize an empty list to store the sales data
    sales_data = []
    
    # Loop through each product and category combination
    for product in product_list:
        for category in categories:
            # Generate random quantity sold between 1 and 100
            quantity_sold = random.randint(1, 100)
            
            # Generate random revenue per unit between 10 and 100
            revenue_per_unit = random.randint(10, 100)
            
            # Calculate total revenue
            total_revenue = quantity_sold * revenue_per_unit
            
            # Append the data to the sales_data list
            sales_data.append({
                'Product': product,
                'Category': category,
                'Quantity Sold': quantity_sold,
                'Revenue': total_revenue
            })
    
    # Create a DataFrame from the sales_data list
    df = pd.DataFrame(sales_data)
    
    return df