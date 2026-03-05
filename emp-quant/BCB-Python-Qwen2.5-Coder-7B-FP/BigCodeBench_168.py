import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def task_func(num_groups=5, data_size=5, labels=None):
    """
    Generates random data and visualizes it with a stacked bar chart, saving the chart to a file.
    
    Parameters:
    - num_groups (int): The number of groups in the data.
    - data_size (int): The number of data points per group.
    - labels (list of str): Optional list of labels for the groups.
    
    Returns:
    - tuple: A tuple containing:
        matplotlib.figure.Figure: The Figure object containing the stacked bar chart.
        pandas.DataFrame: The DataFrame with randomly generated data.
        str: The filename where the plot is saved ('test_plot.png').
    """
    # Generate random data
    np.random.seed(0)  # For reproducibility
    data = np.random.randint(1, 10, size=(data_size, num_groups))
    df = pd.DataFrame(data, columns=labels if labels else [f'Group {i+1}' for i in range(num_groups)])
    
    # Create a stacked bar chart
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title('Stacked Bar Chart of Random Data')
    ax.set_xlabel('Data Points')
    ax.set_ylabel('Values')
    
    # Save the plot to a file
    filename = 'test_plot.png'
    plt.savefig(filename)
    
    return fig, df, filename