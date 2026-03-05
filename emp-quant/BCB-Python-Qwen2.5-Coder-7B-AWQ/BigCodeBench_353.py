import pandas as pd
import random
def task_func(product_list, categories, min_value=10, max_value=100):
    # Initialize an empty list to store the sales data
    sales_data = []
    
    # Loop through each product and category to generate sales data
    for product in product_list:
        for category in categories:
            # Generate random quantity sold and revenue for each product
            quantity_sold = random.randint(min_value, max_value)
            revenue = random.randint(min_value, max_value)
            total_revenue = quantity_sold * revenue
            
            # Append the sales data to the list
            sales_data.append({
                'Product': product,
                'Category': category,
                'Quantity Sold': quantity_sold,
                'Revenue': revenue,
                'Total Revenue': total_revenue
            })
    
    # Create a pandas DataFrame from the sales data
    sales_df = pd.DataFrame(sales_data)
    
    return sales_df