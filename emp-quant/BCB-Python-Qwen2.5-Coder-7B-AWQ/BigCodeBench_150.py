import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(product_dict, product_keys):
    # Create a list to store product data
    product_data = []
    
    # Calculate total quantity, total price, and total profit
    total_quantity = 0
    total_price = 0
    total_profit = 0
    
    # Iterate over the product keys and extract data
    for key in product_keys:
        if key in product_dict:
            quantity = product_dict[key]['Quantity']
            price = product_dict[key]['Price']
            profit = product_dict[key]['Profit']
            
            # Append product data to the list
            product_data.append([key, quantity, price, profit])
            
            # Update total quantities, prices, and profits
            total_quantity += quantity
            total_price += price
            total_profit += profit
    
    # Create a DataFrame from the product data
    df = pd.DataFrame(product_data, columns=['Product', 'Quantity', 'Price', 'Profit'])
    
    # Calculate average price and profit
    average_price = total_price / total_quantity if total_quantity > 0 else 0
    average_profit = total_profit / len(product_data) if len(product_data) > 0 else 0
    
    # Add average price and profit columns to the DataFrame
    df['Average Price'] = average_price
    df['Average Profit'] = average_profit
    
    # Create a bar chart of the profit for each product
    if len(product_data) > 0:
        fig, ax = plt.subplots()
        ax.bar(df['Product'], df['Profit'], color='blue')
        ax.set_xlabel('Product')
        ax.set_ylabel('Profit')
        ax.set_title('Profit Report')
        return df, ax
    else:
        return df, None