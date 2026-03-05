
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(my_list, seed=42):
    # Check if my_list is a list
    if not isinstance(my_list, list):
        raise TypeError("my_list must be a list")
    
    # Add "12" to the list
    my_list.append(12)
    
    # Define the categories
    categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate random sales data
    sales_data = pd.DataFrame({
        'Category': np.random.choice(categories, size=100),
        'Sales': np.random.randint(10, 100, size=100)
    })
    
    # Plot the bar plot
    fig, ax = plt.subplots()
    sales_data.groupby('Category')['Sales'].mean().plot(kind='bar', ax=ax)
    ax.set_xlabel('Category')
    ax.set_ylabel('Average Sales')
    ax.set_title('Average Sales by Category')
    
    # Return the DataFrame and the plot
    return sales_data, ax