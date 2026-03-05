import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(product_dict, product_keys):
    # Create a DataFrame with columns ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']
    df = pd.DataFrame(columns=['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit'])

    # Calculate the profit for each product and add it to the DataFrame
    for product in product_keys:
        quantity = product_dict[product]['quantity']
        price = product_dict[product]['price']
        profit = product_dict[product]['profit']
        average_price = np.mean(price)
        average_profit = np.mean(profit)
        df = df.append({'Product': product, 'Quantity': quantity, 'Price': price, 'Profit': profit, 'Average Price': average_price, 'Average Profit': average_profit}, ignore_index=True)

    # Calculate the average price and profit for all considered products
    average_price = np.mean(df['Price'])
    average_profit = np.mean(df['Profit'])

    # Plot a bar chart of the profit for each product
    fig, ax = plt.subplots()
    ax.bar(df['Product'], df['Profit'])
    ax.set_title('Profit for each product')
    ax.set_xlabel('Product')
    ax.set_ylabel('Profit')
    plt.show()

    return df, ax
product_dict = {'Product 1': {'quantity': 10, 'price': 100, 'profit': 10},
                'Product 2': {'quantity': 20, 'price': 200, 'profit': 20},
                'Product 3': {'quantity': 30, 'price': 300, 'profit': 30}}
product_keys = list(product_dict.keys())