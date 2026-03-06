
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

PRODUCTS = ['Product' + str(i) for i in range(1, 6)]
MONTHS = ['Month' + str(i) for i in range(1, 13)]

def task_func():
    # Generate random sales data
    sales_data = np.random.randint(100, 1000, size=(len(MONTHS), len(PRODUCTS)))
    df = pd.DataFrame(sales_data, index=MONTHS, columns=PRODUCTS)
    
    # Calculate total sales per product
    total_sales_per_product = df.sum()
    
    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    # Line plot for total sales per product
    axes[0].plot(total_sales_per_product.index, total_sales_per_product.values, marker='o')
    axes[0].set_title('Total Sales Per Product')
    axes[0].set_xlabel('Products')
    axes[0].set_ylabel('Sales')
    
    # Heatmap for sales figures
    sns.heatmap(df, annot=True, fmt="d", cmap='YlGnBu', ax=axes[1])
    axes[1].set_title('Sales Figures Across Products and Months')
    axes[1].set_xlabel('Products')
    axes[1].set_ylabel('Months')
    
    plt.tight_layout()
    plt.show()
    
    return df