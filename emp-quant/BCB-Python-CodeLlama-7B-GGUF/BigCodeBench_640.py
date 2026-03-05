
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

PRODUCTS = ['Product' + str(i) for i in range(1, 6)]
MONTHS = ['Month' + str(i) for i in range(1, 13)]

def task_func():
    # Generate random sales figures for each product over 12 months
    sales_data = np.random.randint(100, size=(12, 5))
    sales_df = pd.DataFrame(sales_data, columns=PRODUCTS, index=MONTHS)

    # Plot total sales per product using a line plot
    sns.set(style="whitegrid")
    sns.lineplot(data=sales_df, x=MONTHS, y=PRODUCTS)
    plt.title("Total Sales per Product")
    plt.xlabel("Month")
    plt.ylabel("Product")
    plt.show()

    # Plot total sales per product using a heatmap
    sns.set(style="whitegrid")
    sns.heatmap(sales_df, annot=True, cmap="YlGnBu")
    plt.title("Sales Heatmap")
    plt.xlabel("Product")
    plt.ylabel("Month")
    plt.show()

    return sales_df

task_func()