
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(product_dict, product_keys):
    # Initialize a list to store product data
    product_data = []
    
    # Iterate through the product keys and extract data from the product dictionary
    for key in product_keys:
        if key in product_dict:
            quantity = product_dict[key]['quantity']
            price = product_dict[key]['price']
            profit = product_dict[key]['profit']
            product_data.append([key, quantity, price, profit])
    
    # Create a pandas DataFrame from the product data
    df = pd.DataFrame(product_data, columns=['Product', 'Quantity', 'Price', 'Profit'])
    
    # Calculate the average price and profit for all products
    average_price = df['Price'].mean()
    average_profit = df['Profit'].mean()
    
    # Add the average price and profit to the DataFrame
    df['Average Price'] = average_price
    df['Average Profit'] = average_profit
    
    # Plot a bar chart of the profit for each product
    fig, ax = plt.subplots()
    df.plot(kind='bar', x='Product', y='Profit', ax=ax)
    ax.set_xlabel('Product')
    ax.set_ylabel('Profit')
    ax.set_title('Profit by Product')
    
    # Return the DataFrame and the plot
    return df, ax

df, ax = task_func(product_dict, product_keys)
print(df)
plt.show()