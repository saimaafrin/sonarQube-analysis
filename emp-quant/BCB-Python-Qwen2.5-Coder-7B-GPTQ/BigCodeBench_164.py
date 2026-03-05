import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def task_func(num_labels=5, data_range=(0, 1)):
    """
    Generate random numeric data across a specified range for a given number of categories and visualize it with a stacked bar chart.
    
    Parameters:
    - num_labels (int): The number of categories.
    - data_range (tuple): A tuple of two integers representing the minimum and maximum values for the data range.
    
    Returns:
    - matplotlib.figure.Figure: A Figure object containing the stacked bar chart of the generated data.
    """
    # Generate random data
    categories = [f'Category {i+1}' for i in range(num_labels)]
    data = np.random.randint(data_range[0], data_range[1] + 1, size=(num_labels, num_labels))
    
    # Create a DataFrame
    df = pd.DataFrame(data, columns=categories)
    
    # Plotting
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title('Stacked Bar Chart of Random Data')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    
    return fig