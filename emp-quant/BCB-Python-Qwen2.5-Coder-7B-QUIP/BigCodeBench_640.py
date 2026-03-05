
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

PRODUCTS = ['Product' + str(i) for i in range(1, 6)]
MONTHS = ['Month' + str(i) for i in range(1, 13)]

def task_func():
    # Generate random sales data
    np.random.seed(0)  # For reproducibility
    sales_data = np.random.randint(100, size=(12, 5))  # 12 months, 5 products

    # Create a DataFrame with the generated sales data
    df = pd.DataFrame(sales_data, index=MONTHS, columns=PRODUCTS)

    # Calculate the total sales per product
    total_sales = df.sum()

    # Plotting the line plot
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, label='Sales per Product')
    plt.title('Total Sales per Product')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.legend()
    plt.show()

    # Plotting the heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(df, annot=True, cmap='viridis')
    plt.title('Sales Heatmap')
    plt.xlabel('Product')
    plt.ylabel('Month')
    plt.show()

    return df