import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(product_dict, product_keys):
    # Create a DataFrame with columns ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']
    df = pd.DataFrame(columns=['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit'])

    # Calculate the average price and profit for all considered products
    average_price = np.mean([product_dict[key]['price'] for key in product_keys])
    average_profit = np.mean([product_dict[key]['profit'] for key in product_keys])

    # Add the average price and profit to the DataFrame
    df.loc[0, 'Average Price'] = average_price
    df.loc[0, 'Average Profit'] = average_profit

    # Add the profit for each product to the DataFrame
    for key in product_keys:
        df.loc[key, 'Product'] = key
        df.loc[key, 'Quantity'] = product_dict[key]['quantity']
        df.loc[key, 'Price'] = product_dict[key]['price']
        df.loc[key, 'Profit'] = product_dict[key]['profit']

    # Plot a bar chart of the profit for each product
    fig, ax = plt.subplots()
    ax.bar(df['Product'], df['Profit'])
    ax.set_xlabel('Product')
    ax.set_ylabel('Profit')
    ax.set_title('Profit for each product')

    return df, ax
product_dict = {'Product 1': {'quantity': 10, 'price': 100, 'profit': 10},
                'Product 2': {'quantity': 20, 'price': 200, 'profit': 20},
                'Product 3': {'quantity': 30, 'price': 300, 'profit': 30}}
product_keys = ['Product 1', 'Product 2', 'Product 3']