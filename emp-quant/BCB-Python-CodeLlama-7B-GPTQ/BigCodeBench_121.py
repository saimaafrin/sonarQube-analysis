import pandas as pd
import numpy as np
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
    # Check if 'my_list' is a list
    if not isinstance(my_list, list):
        raise TypeError("'my_list' must be a list")

    # Simulate sales data for different categories
    categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    sales_data = pd.DataFrame(index=categories, columns=['Sales'])
    for category in categories:
        sales_data.loc[category] = np.random.randint(100, size=10)

    # Add the item "12" to the list
    my_list.append(12)

    # Plot the sales data
    fig, ax = plt.subplots()
    sales_data.plot(kind='bar', ax=ax)
    ax.set_title('Sales Data')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Sales')

    # Return the sales data and the matplotlib Axes object
    return (sales_data, ax)
my_list = [1, 2, 3, 4, 5]