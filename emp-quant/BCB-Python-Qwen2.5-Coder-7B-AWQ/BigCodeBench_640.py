import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
PRODUCTS = ['Product' + str(i) for i in range(1, 6)]
MONTHS = ['Month' + str(i) for i in range(1, 13)]
def task_func():
    # Generate random sales data
    sales_data = np.random.randint(100, 1000, size=(12, 5))
    df = pd.DataFrame(sales_data, columns=PRODUCTS, index=MONTHS)
    
    # Calculate total sales per product
    total_sales = df.sum()
    
    # Plotting the total sales per product
    plt.figure(figsize=(10, 5))
    plt.plot(total_sales, marker='o')
    plt.title('Total Sales per Product')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.show()
    
    # Creating a heatmap for sales figures
    plt.figure(figsize=(10, 8))
    sns.heatmap(df, annot=True, fmt='d', cmap='YlGnBu')
    plt.title('Sales Figures across Products and Months')
    plt.xlabel('Products')
    plt.ylabel('Months')
    plt.show()
    
    return df