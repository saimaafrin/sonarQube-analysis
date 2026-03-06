
import pandas as pd
import random

def task_func(product_list, categories, min_value=10, max_value=100):
    # Create a dictionary to store the sales data
    sales_data = {}

    # Loop through the product list and generate random sales data
    for product in product_list:
        # Generate a random quantity sold for the product
        quantity_sold = random.randint(min_value, max_value)

        # Generate a random revenue for the product
        revenue = quantity_sold * random.randint(min_value, max_value)

        # Add the sales data for the product to the dictionary
        sales_data[product] = {
            'Quantity Sold': quantity_sold,
            'Revenue': revenue
        }

    # Create a pandas DataFrame from the sales data dictionary
    df = pd.DataFrame(sales_data)

    # Add the category column to the DataFrame
    df['Category'] = categories

    return df

# Generate random sales data for the products
df = task_func(product_list, categories)

# Print the sales data
print(df)