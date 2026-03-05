import pandas as pd
import matplotlib.pyplot as plt
from random import randint
def task_func(num_types=5, integer_range=(0, 100)):
    """
    Generate a DataFrame containing random integer values across a specified number of categories, and visualize these data as a horizontal stacked bar chart.
    """
    # Generate random data
    data = []
    for i in range(num_types):
        data.append(pd.Series(randint(integer_range[0], integer_range[1], size=10)))
    df = pd.concat(data, axis=1)

    # Visualize data
    fig, ax = plt.subplots()
    ax.barh(df.index, df.iloc[:, 0], color='blue')
    for i in range(1, num_types):
        ax.barh(df.index, df.iloc[:, i], bottom=df.iloc[:, i-1], color='red')
    ax.set_xlabel('Values')
    ax.set_ylabel('Categories')
    ax.set_title('Horizontal Stacked Bar Chart')
    return fig, ax