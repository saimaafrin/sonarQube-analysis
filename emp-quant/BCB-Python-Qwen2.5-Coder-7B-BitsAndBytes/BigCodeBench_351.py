
import pandas as pd
import random

def task_func(product_list, categories, min_value=10, max_value=100):
    # Create an empty list to store the sales data
    sales_data = []
    
    # Loop through each product and category combination
    for product in product_list:
        for category in categories:
            # Generate random quantity sold and revenue
            quantity_sold = random.randint(min_value, max_value)
            revenue = round(quantity_sold * random.uniform(10, 100), 2)  # Assuming price per unit is between $10 and $100
            
            # Append the data to the list
            sales_data.append({
                'Product': product,
                'Category': category,
                'Quantity Sold': quantity_sold,
                'Revenue': revenue
            })
    
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(sales_data)
    
    return df