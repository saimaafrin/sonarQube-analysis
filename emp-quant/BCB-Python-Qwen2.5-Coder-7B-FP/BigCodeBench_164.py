import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def task_func(num_labels=5, data_range=(0, 1)):
    """
    Generates random numeric data across a specified range for a given number of categories
    and visualizes it with a stacked bar chart.

    Parameters:
    - num_labels (int): The number of categories.
    - data_range (tuple): A tuple of two integers representing the minimum and maximum values of the data range.

    Returns:
    - matplotlib.figure.Figure: A Figure object containing the stacked bar chart of the generated data.
    """
    # Generate random data
    labels = [f'Label {i+1}' for i in range(num_labels)]
    data = np.random.randint(data_range[0], data_range[1] + 1, size=(num_labels, num_labels))
    data = np.cumsum(data, axis=1)  # Ensure data is non-negative and cumulative

    # Create DataFrame
    df = pd.DataFrame(data, columns=labels, index=labels)

    # Plotting
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, ax=ax)
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    ax.set_title('Stacked Bar Chart of Random Data')
    ax.legend(title='Labels')

    return fig