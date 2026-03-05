
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(product_dict, product_keys):
    # Extract data from product_dict based on product_keys
    data = {key: product_dict[key] for key in product_keys if key in product_dict}
    
    # Create DataFrame from the extracted data
    df = pd.DataFrame(list(data.items()), columns=['Product', 'Details'])
    df['Quantity'] = df['Details'].apply(lambda x: x['Quantity'])
    df['Price'] = df['Details'].apply(lambda x: x['Price'])
    df['Profit'] = df['Details'].apply(lambda x: x['Profit'])
    
    # Calculate average price and profit
    avg_price = df['Price'].mean()
    avg_profit = df['Profit'].mean()
    
    # Add average price and profit to DataFrame
    df['Average Price'] = avg_price
    df['Average Profit'] = avg_profit
    
    # Plot bar chart of profit for each product
    if not df.empty:
        fig, ax = plt.subplots()
        ax.bar(df['Product'], df['Profit'], color='blue')
        ax.set_xlabel('Product')
        ax.set_ylabel('Profit')
        ax.set_title('Profit Report for Products')
        plt.xticks(rotation=45)
        plt.tight_layout()
    else:
        fig, ax = None
    
    # Return tuple containing DataFrame and Axes object
    return df[['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']], ax