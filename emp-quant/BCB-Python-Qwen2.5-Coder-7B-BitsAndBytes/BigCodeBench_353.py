
import pandas as pd
import random

def task_func(product_list, categories, min_value=10, max_value=100):
    # Create an empty list to store the sales data
    sales_data = []
    
    # Loop through each product and category combination
    for product in product_list:
        for category in categories:
            # Generate random values for Quantity Sold and Revenue
            quantity_sold = random.randint(min_value, max_value)
            revenue_per_product = random.uniform(10, 1000)  # Assuming revenue is between $10 and $1000
            
            # Calculate Total Revenue
            total_revenue = quantity_sold * revenue_per_product
            
            # Append the data to the list
            sales_data.append({
                'Product': product,
                'Category': category,
                'Quantity Sold': quantity_sold,
                'Revenue': revenue_per_product,
                'Total Revenue': total_revenue
            })
    
    # Convert the list to a DataFrame
    df = pd.DataFrame(sales_data)
    
    return df