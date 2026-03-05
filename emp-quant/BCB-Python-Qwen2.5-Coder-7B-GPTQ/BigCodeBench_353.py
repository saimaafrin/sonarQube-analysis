import pandas as pd
import random
def task_func(product_list, categories, min_value=10, max_value=100):
    # Initialize an empty list to store the data
    data = []
    
    # Loop through each product and category
    for product in product_list:
        for category in categories:
            # Generate random quantity sold and revenue
            quantity_sold = random.randint(min_value, max_value)
            revenue = random.randint(min_value, max_value)
            total_revenue = quantity_sold * revenue
            
            # Append the data to the list
            data.append([product, category, quantity_sold, revenue, total_revenue])
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['Product', 'Category', 'Quantity Sold', 'Revenue', 'Total Revenue'])
    
    return df
product_list = ['Product A', 'Product B', 'Product C']
categories = ['Category X', 'Category Y']