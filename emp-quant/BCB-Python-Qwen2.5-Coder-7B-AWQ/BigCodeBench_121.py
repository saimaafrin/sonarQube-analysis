import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(my_list, seed=42):
    """
    Adds an item "12" to a list 'my_list', simulates sales data for different categories with an optional seed for reproducibility,
    and returns the data along with a bar plot.
    
    Parameters:
    my_list (list): A list to which "12" will be added.
    seed (int, optional): Seed for reproducibility of random sales data. Defaults to 42.
    
    Returns:
    tuple: A tuple containing a pandas DataFrame of simulated sales data and the corresponding matplotlib Axes object.
    """
    # Check if my_list is a list
    if not isinstance(my_list, list):
        raise TypeError("my_list must be a list")
    
    # Add "12" to the list
    my_list.append("12")
    
    # Define categories
    categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Simulate sales data
    sales_data = np.random.randint(100, 1000, size=len(categories))
    sales_df = pd.DataFrame({'Category': categories, 'Sales': sales_data})
    
    # Create a bar plot
    fig, ax = plt.subplots()
    ax.bar(sales_df['Category'], sales_df['Sales'], color='blue')
    ax.set_xlabel('Category')
    ax.set_ylabel('Sales')
    ax.set_title('Simulated Sales Data')
    
    return sales_df, ax