import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def task_func(num_labels=5, data_range=(0, 1)):
    """
    Generate random numeric data across a specified range for a given number of categories and visualize it with a stacked bar chart.
    """
    # Generate random data
    data = np.random.randint(data_range[0], data_range[1], size=(num_labels,))

    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['Values'])

    # Create a stacked bar chart
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, ax=ax)

    # Set the title and labels
    ax.set_title('Stacked Bar Chart')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')

    # Show the plot
    fig.show()
num_labels = 3
data_range = (1, 10)