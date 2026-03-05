
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(num_groups=5, data_size=5, labels=None):
    # Generate random data
    if labels is None:
        labels = [f'Group {i}' for i in range(num_groups)]
    data = np.random.rand(data_size, num_groups)
    
    # Create a DataFrame to hold the data
    df = pd.DataFrame(data, columns=labels)
    
    # Create a stacked bar chart
    fig, ax = plt.subplots()
    ax.bar(range(num_groups), data.sum(axis=0), label='Data')
    ax.set_xlabel('Groups')
    ax.set_ylabel('Values')
    ax.set_title('Stacked Bar Chart')
    ax.legend()
    
    # Save the plot to a file
    filename = 'test_plot.png'
    plt.savefig(filename)
    
    # Return the figure, DataFrame, and filename
    return fig, df, filename