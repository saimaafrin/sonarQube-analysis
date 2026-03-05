
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
            revenue_per_product = random.randint(min_value, max_value)
            total_revenue = quantity_sold * revenue_per_product
            
            # Append the sales data to the list
            sales_data.append({
                'Product': product,
                'Category': category,
                'Quantity Sold': quantity_sold,
                'Revenue': revenue_per_product,
                'Total Revenue': total_revenue
            })
    
    # Create a DataFrame from the sales data
    sales_df = pd.DataFrame(sales_data)
    
    return sales_df