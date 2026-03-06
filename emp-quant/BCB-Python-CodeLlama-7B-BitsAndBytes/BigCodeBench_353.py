
import pandas as pd
import random

def task_func(product_list, categories, min_value=10, max_value=100):
    # Create a dictionary to store the sales data
    sales_data = {}

    # Loop through each product and category
    for product, category in product_list:
        # Generate random quantity sold and revenue for the product
        quantity_sold = random.randint(min_value, max_value)
        revenue = quantity_sold * random.randint(min_value, max_value)

        # Add the sales data to the dictionary
        sales_data[product] = {
            'Category': category,
            'Quantity Sold': quantity_sold,
            'Revenue': revenue,
            'Total Revenue': revenue
        }

    # Create a pandas DataFrame from the sales data dictionary
    df = pd.DataFrame(sales_data)

    # Return the DataFrame
    return df

# Generate random sales data for each product
df = task_func(product_list, categories)

# Print the sales data
print(df)