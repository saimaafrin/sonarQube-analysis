
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(product_dict, product_keys):
    # Create a DataFrame with the product data
    df = pd.DataFrame(product_dict, index=product_keys)

    # Calculate the average price and profit for all products
    average_price = df['Price'].mean()
    average_profit = df['Profit'].mean()

    # Calculate the profit for each product
    df['Profit'] = df['Quantity'] * df['Price'] - df['Profit']

    # Plot a bar chart of the profit for each product
    fig, ax = plt.subplots()
    ax.bar(df['Product'], df['Profit'])
    ax.set_xlabel('Product')
    ax.set_ylabel('Profit')
    ax.set_title('Profit Report')

    # Return the DataFrame and the Axes object
    return (df, ax)

# Call the function and print the results
df, ax = task_func(product_dict, product_keys)
print(df)
print(ax)