import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(my_list, seed=42):
    """
    Adds an item "12" to a list 'my_list', simulates sales data for different categories with an optional seed for reproducibility, and returns the data along with a bar plot.
    The sales data is a DataFrame with random sales figures for predefined categories.
    The categories are 'Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports'.
    The function should raise the exception for:
        TypeError: If 'my_list' is not a list.
    The function should output with:
        tuple: A tuple containing a pandas DataFrame of simulated sales data and the corresponding matplotlib Axes object.
    """
    if not isinstance(my_list, list):
        raise TypeError("'my_list' must be a list")

    np.random.seed(seed)
    categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    sales_data = pd.DataFrame(
        np.random.randint(100, size=(len(categories), len(categories))),
        columns=categories,
        index=categories
    )
    sales_data.loc['12'] = 12
    fig, ax = plt.subplots()
    sales_data.plot(kind='bar', ax=ax)
    return sales_data, ax