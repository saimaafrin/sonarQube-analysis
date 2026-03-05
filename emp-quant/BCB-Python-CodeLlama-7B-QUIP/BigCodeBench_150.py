
import pandas as pd
import numpy as np

def task_func(product_dict, product_keys):
    # Create a DataFrame with the given product_dict
    df = pd.DataFrame(product_dict)

    # Calculate the average price and profit for all products
    df['Average Price'] = df['Quantity'] * df['Price'] / df['Quantity'].sum()
    df['Average Profit'] = df['Profit'] / df['Quantity'].sum()

    # Plot a bar chart of the profit for each product
    fig, ax = plt.subplots()
    ax.bar(df['Product'], df['Profit'])
    ax.set_ylabel('Profit')
    ax.set_xlabel('Product')
    ax.set_title('Profit Report')

    return df, fig