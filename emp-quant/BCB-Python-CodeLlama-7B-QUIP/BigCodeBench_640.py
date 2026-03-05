
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

PRODUCTS = ['Product' + str(i) for i in range(1, 6)]
MONTHS = ['Month' + str(i) for i in range(1, 13)]

def task_func():
    # Generate a DataFrame with randomly generated sales figures for each product over 12 months
    sales_df = pd.DataFrame(np.random.randint(100, size=(12, 5)), columns=PRODUCTS)
    sales_df.index = MONTHS

    # Plot the total sales per product
    plt.figure(figsize=(10, 6))
    sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(sns.heatmap(s