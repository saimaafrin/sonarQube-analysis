import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(product_dict, product_keys):
    # Extract data from product_dict based on product_keys
    data = {key: product_dict[key] for key in product_keys if key in product_dict}
    
    # Create a DataFrame from the extracted data
    df = pd.DataFrame(list(data.items()), columns=['Product', 'Details'])
    
    # Split the 'Details' column into separate columns for Quantity, Price, and Profit
    df[['Quantity', 'Price', 'Profit']] = pd.DataFrame(df['Details'].tolist(), index=df.index)
    
    # Convert the extracted values to numeric types
    df['Quantity'] = pd.to_numeric(df['Quantity'])
    df['Price'] = pd.to_numeric(df['Price'])
    df['Profit'] = pd.to_numeric(df['Profit'])
    
    # Calculate the average price and profit for all products
    average_price = df['Price'].mean()
    average_profit = df['Profit'].mean()
    
    # Add the average price and profit to each row in the DataFrame
    df['Average Price'] = average_price
    df['Average Profit'] = average_profit
    
    # Plot a bar chart of the profit for each product
    if not df.empty:
        ax = df.plot(kind='bar', x='Product', y='Profit', legend=False)
        ax.set_xlabel('Product')
        ax.set_ylabel('Profit')
        ax.set_title('Profit Report')
    else:
        ax = None
    
    # Return the DataFrame and the Axes object
    return df, ax