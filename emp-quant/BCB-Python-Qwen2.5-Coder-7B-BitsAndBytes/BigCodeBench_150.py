
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(product_dict, product_keys):
    # Create a DataFrame from the product dictionary
    df = pd.DataFrame(list(product_dict.items()), columns=['Product', 'Details'])
    
    # Extract details into separate columns
    df[['Quantity', 'Price', 'Profit']] = pd.DataFrame(df['Details'].tolist(), index=df.index)
    
    # Convert data types to appropriate values
    df['Quantity'] = df['Quantity'].astype(int)
    df['Price'] = df['Price'].astype(float)
    df['Profit'] = df['Profit'].astype(float)
    
    # Calculate total number of products
    total_products = len(df)
    
    # Calculate average price and profit
    average_price = df['Price'].mean()
    average_profit = df['Profit'].mean()
    
    # Add average price and profit columns to the DataFrame
    df['Average Price'] = average_price
    df['Average Profit'] = average_profit
    
    # Filter products based on product keys
    filtered_df = df[df['Product'].isin(product_keys)]
    
    # Plotting the bar chart
    if not filtered_df.empty:
        fig, ax = plt.subplots()
        filtered_df.plot(kind='bar', x='Product', y='Profit', ax=ax)
        ax.set_title('Profit Report')
        ax.set_xlabel('Products')
        ax.set_ylabel('Profit')
        return (filtered_df, ax)
    else:
        return (df, None)