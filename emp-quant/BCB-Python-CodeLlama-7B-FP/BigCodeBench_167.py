import pandas as pd
import matplotlib.pyplot as plt
from random import randint
def task_func(num_types=5, integer_range=(0, 100)):
    """
    Generate a DataFrame containing random integer values across a specified number of categories, and visualize these data as a horizontal stacked bar chart.
    """
    # Generate random data
    data = {f"Type {i}": [randint(integer_range[0], integer_range[1]) for _ in range(num_types)] for i in range(num_types)}
    df = pd.DataFrame(data)

    # Visualize data
    fig, ax = plt.subplots()
    ax.barh(df.index, df.values, color="C0")
    ax.set_xlabel("Values")
    ax.set_ylabel("Categories")
    ax.set_title("Horizontal Stacked Bar Chart")
    ax.legend(loc="upper left")
    return fig, ax