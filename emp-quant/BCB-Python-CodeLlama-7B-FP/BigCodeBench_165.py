import pandas as pd
import matplotlib.pyplot as plt
from random import randint
def task_func(num_rows=5, rand_range=(0, 100)):
    """
    Create a DataFrame containing random integer values within a specified range for categories 'A' through 'E', and visualize this data with a stacked bar chart.
    """
    # Create a list of random integers within the specified range
    data = [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)]

    # Create a DataFrame with the random integers
    df = pd.DataFrame({'A': data, 'B': data, 'C': data, 'D': data, 'E': data})

    # Visualize the data with a stacked bar chart
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, ax=ax)

    # Set the title and labels
    ax.set_title('Stacked Bar Chart')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')

    # Return the matplotlib Figure object
    return fig
num_rows = 10
rand_range = (0, 100)