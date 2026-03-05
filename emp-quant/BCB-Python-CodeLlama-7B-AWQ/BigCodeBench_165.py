import pandas as pd
import matplotlib.pyplot as plt
from random import randint
def task_func(num_rows=5, rand_range=(0, 100)):
    """
    Create a DataFrame containing random integer values within a specified range for categories 'A' through 'E', and visualize this data with a stacked bar chart.
    """
    # Create a list of random integers within the specified range for each category
    data = {
        'A': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'B': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'C': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'D': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'E': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)]
    }

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data)

    # Visualize the data with a stacked bar chart
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title('Stacked Bar Chart of Random Integers')
    ax.set_xlabel('Category')
    ax.set_ylabel('Value')
    ax.set_xticks(range(len(df.columns)))
    ax.set_xticklabels(df.columns)
    plt.show()

    return fig