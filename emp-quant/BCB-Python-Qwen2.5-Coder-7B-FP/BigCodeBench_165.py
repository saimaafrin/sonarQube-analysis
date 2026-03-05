import pandas as pd
import matplotlib.pyplot as plt
from random import randint
def task_func(num_rows=5, rand_range=(0, 100)):
    """
    Generates a DataFrame with random integer values within a specified range for categories 'A' through 'E',
    and plots this data with a stacked bar chart.

    Parameters:
    - num_rows (int): The number of rows in the DataFrame.
    - rand_range (tuple): A tuple containing the lower and upper bounds for the random integer range.

    Returns:
    - matplotlib.figure.Figure: The matplotlib Figure object containing the plotted data.
    """
    # Create a DataFrame with random integer values for categories 'A' through 'E'
    data = {chr(65 + i): [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)] for i in range(5)}
    df = pd.DataFrame(data)

    # Plot the data with a stacked bar chart
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, ax=ax)
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    ax.set_title('Stacked Bar Chart of Random Integer Values')

    return fig