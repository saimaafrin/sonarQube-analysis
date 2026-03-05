import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(product_dict, product_keys):
    # Create a DataFrame from the product dictionary
    df = pd.DataFrame(list(product_dict.items()), columns=['Product', 'Details'])
    
    # Extract the necessary details from the 'Details' column
    df[['Quantity', 'Price', 'Profit']] = pd.DataFrame(df['Details'].tolist(), index=df.index)
    
    # Convert the extracted details to appropriate data types
    df['Quantity'] = df['Quantity'].astype(int)
    df['Price'] = df['Price'].astype(float)
    df['Profit'] = df['Profit'].astype(float)
    
    # Calculate the average price and profit
    average_price = df['Price'].mean()
    average_profit = df['Profit'].mean()
    
    # Add the average price and profit to the DataFrame
    df['Average Price'] = average_price
    df['Average Profit'] = average_profit
    
    # Plot a bar chart of the profit for each product
    if not df.empty:
        fig, ax = plt.subplots()
        ax.bar(df['Product'], df['Profit'], color='blue')
        ax.set_xlabel('Product')
        ax.set_ylabel('Profit')
        ax.set_title('Profit Report')
        plt.xticks(rotation=45)
        plt.tight_layout()
    else:
        fig, ax = None, None
    
    # Return the DataFrame and the Axes object
    return df[['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']], ax