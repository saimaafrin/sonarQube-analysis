import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def task_func(num_groups=5, data_size=5, labels=None):
    """
    Generate random data and visualize it with a stacked bar chart, saving the chart to a file.

    Args:
        num_groups (int): Number of groups to generate data for.
        data_size (int): Size of each group.
        labels (list): List of labels for each group.

    Returns:
        tuple: A tuple containing:
            matplotlib.figure.Figure: The Figure object containing the stacked bar chart.
            pandas.DataFrame: The DataFrame with randomly generated data.
            str: The filename where the plot is saved ('test_plot.png').
    """
    # Generate random data
    data = np.random.randint(0, 100, size=(num_groups, data_size))
    df = pd.DataFrame(data, columns=labels)

    # Create stacked bar chart
    fig, ax = plt.subplots()
    ax.bar(df.index, df.sum(axis=1), label='Total')
    ax.bar(df.index, df.iloc[:, 0], label='Group 1')
    ax.bar(df.index, df.iloc[:, 1], label='Group 2')
    ax.bar(df.index, df.iloc[:, 2], label='Group 3')
    ax.bar(df.index, df.iloc[:, 3], label='Group 4')
    ax.bar(df.index, df.iloc[:, 4], label='Group 5')
    ax.set_xlabel('Group')
    ax.set_ylabel('Data')
    ax.set_title('Stacked Bar Chart')
    ax.legend()

    # Save plot to file
    fig.savefig('test_plot.png')

    return fig, df, 'test_plot.png'