import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
PRODUCTS = ['Product' + str(i) for i in range(1, 6)]
MONTHS = ['Month' + str(i) for i in range(1, 13)]
def task_func():
    # Generate random sales figures for each product over 12 months
    sales_data = np.random.randint(100, size=(12, 5))

    # Create a DataFrame with sales data
    df = pd.DataFrame(sales_data, columns=PRODUCTS, index=MONTHS)

    # Plot total sales per product using a line plot
    plt.plot(df.sum(axis=0))
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.title('Total Sales per Product')
    plt.show()

    # Plot total sales per month using a heatmap
    sns.heatmap(df.sum(axis=1), annot=True, cmap='coolwarm')
    plt.xlabel('Month')
    plt.ylabel('Product')
    plt.title('Total Sales per Month')
    plt.show()

    return df