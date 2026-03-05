import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(product_dict, product_keys):
    # Create a DataFrame with columns ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']
    df = pd.DataFrame(columns=['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit'])

    # Calculate the profit for each product
    for product in product_keys:
        quantity = product_dict[product]['quantity']
        price = product_dict[product]['price']
        profit = quantity * price
        df = df.append({'Product': product, 'Quantity': quantity, 'Price': price, 'Profit': profit}, ignore_index=True)

    # Calculate the average price and profit for all considered products
    average_price = df['Price'].mean()
    average_profit = df['Profit'].mean()

    # Plot a bar chart of the profit for each product
    fig, ax = plt.subplots()
    ax.bar(df['Product'], df['Profit'])
    ax.set_ylabel('Profit')
    ax.set_xlabel('Product')
    ax.set_title('Profit for Each Product')

    return (df, ax)
product_dict = {'Product 1': {'quantity': 10, 'price': 10},
                'Product 2': {'quantity': 20, 'price': 20},
                'Product 3': {'quantity': 30, 'price': 30}}
product_keys = ['Product 1', 'Product 2', 'Product 3']