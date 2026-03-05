import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(my_list, seed=42):
    # Check if my_list is a list
    if not isinstance(my_list, list):
        raise TypeError("my_list must be a list")
    
    # Add "12" to the list
    my_list.append("12")
    
    # Define categories
    categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate random sales data
    sales_data = np.random.randint(100, 1000, size=(len(categories), 12))
    
    # Create a DataFrame
    df = pd.DataFrame(sales_data, columns=[f'Month {i+1}' for i in range(12)], index=categories)
    
    # Plot the data
    fig, ax = plt.subplots()
    df.plot(kind='bar', ax=ax)
    ax.set_title('Simulated Sales Data')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Sales')
    
    # Return the DataFrame and the Axes object
    return df, ax