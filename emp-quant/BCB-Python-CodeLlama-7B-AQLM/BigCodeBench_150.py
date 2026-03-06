import pandas as pd
import numpy as np
def task_func(product_dict, product_keys):
    """
    Create a profit report for a list of products based on a specific product dictionary that includes the quantity,
    price, and profit of each product. Additionally, calculate the average price and profit for all considered products,
    and plot a bar chart of the profit for each product.

    Parameters:
    - product_dict (dict): The dictionary containing product details with product name as key and a list
    [quantity, price] as value.
    - product_keys (list): The list of product keys to consider for the report.

    Returns: tuple: A tuple containing:
    - DataFrame: A pandas DataFrame with columns
    ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit'].
    - Axes: A matplotlib Axes object representing the plotted bar chart of profit for each product
    (None if no products).

    Requirements:
    - pandas
    - numpy

    Example:
    >>> product_dict = {'Apple': [100, 2.5], 'Orange': [80, 3.5], 'Banana': [120, 1.5]}
    >>> product_keys = ['Apple', 'Banana']
    >>> report, ax = task_func(product_dict, product_keys)
    >>> print(report)
      Product  Quantity  Price  Profit  Average Price  Average Profit
    0   Apple       100    2.5   250.0            2.0           215.0
    1  Banana       120    1.5   180.0            2.0           215.0

    """
    # TODO: Implement task_func
    # Hint: Use the following code to create a DataFrame with the required columns
    # df = pd.DataFrame(columns=['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit'])
    # Hint: Use the following code to calculate the average price and profit for all considered products
    # average_price = np.mean([product_dict[key][1] for key in product_keys])
    # average_profit = np.mean([product_dict[key][1] * product_dict[key][0] for key in product_keys])
    # Hint: Use the following code to calculate the profit for each product
    # profit = product_dict[key][1] * product_dict[key][0]
    # Hint: Use the following code to create a bar chart of profit for each product
    # ax = df.plot.bar(x='Product', y='Profit', rot=0)
    # Hint: Use the following code to add the average price and profit to the DataFrame
    # df['Average Price'] = average_price
    # df['Average Profit'] = average_profit
    # Hint: Use the following code to return the DataFrame and the bar chart
    # return df, ax