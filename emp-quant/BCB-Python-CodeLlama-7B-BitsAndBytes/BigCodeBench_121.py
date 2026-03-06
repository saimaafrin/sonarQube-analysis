
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(my_list, seed=42):
    if not isinstance(my_list, list):
        raise TypeError("'my_list' must be a list")

    # Simulate sales data for different categories
    np.random.seed(seed)
    sales_data = pd.DataFrame({
        'Electronics': np.random.normal(100, 20, size=10),
        'Fashion': np.random.normal(80, 15, size=10),
        'Home & Kitchen': np.random.normal(60, 10, size=10),
        'Automotive': np.random.normal(40, 5, size=10),
        'Sports': np.random.normal(20, 3, size=10)
    })

    # Add the item "12" to the list
    my_list.append(12)

    # Plot the sales data
    fig, ax = plt.subplots()
    sales_data.plot(kind='bar', ax=ax)
    ax.set_title('Sales Data')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Sales')
    ax.legend()

    return sales_data, ax