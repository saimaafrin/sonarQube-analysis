
import pandas as pd
import random

def task_func(product_list, categories):
    # Create a dictionary to store the sales data
    sales_data = {}

    # Loop through the product list and generate random sales data
    for product in product_list:
        # Generate a random quantity sold for the product
        quantity_sold = random.randint(1, 100)

        # Generate a random revenue for the product
        revenue = quantity_sold * random.randint(10, 100)

        # Add the sales data for the product to the dictionary
        sales_data[product] = {
            'Quantity Sold': quantity_sold,
            'Revenue': revenue
        }

    # Create a pandas DataFrame from the sales data dictionary
    sales_df = pd.DataFrame.from_dict(sales_data, orient='index')

    # Sort the DataFrame by revenue
    sales_df = sales_df.sort_values(by='Revenue', ascending=False)

    # Return the sorted DataFrame
    return sales_df