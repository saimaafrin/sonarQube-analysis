
import pandas as pd
import random

def task_func(product_list, categories):
    # Create a dictionary to store the sales data
    sales_data = {}

    # Loop through the product list and generate random sales data
    for product in product_list:
        # Generate random quantity sold and revenue
        quantity_sold = random.randint(1, 100)
        revenue = quantity_sold * random.randint(10, 100)

        # Add the sales data to the dictionary
        sales_data[product] = {
            'Category': categories[product],
            'Quantity Sold': quantity_sold,
            'Revenue': revenue
        }

    # Create a pandas DataFrame from the sales data dictionary
    sales_df = pd.DataFrame.from_dict(sales_data, orient='index')

    # Return the DataFrame
    return sales_df

sales_df = task_func(product_list, categories)
print(sales_df)