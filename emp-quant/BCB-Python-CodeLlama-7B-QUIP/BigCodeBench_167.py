
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def task_func(num_types=5, integer_range=(0, 100)):
    # Generate a DataFrame with random integer values across the specified number of categories
    data = {
        'Category': [f'Category {i}' for i in range(num_types)],
        'Values': [randint(integer_range[0], integer_range[1]) for i in range(num_types)]
    }
    df = pd.DataFrame(data)

    # Visualize the DataFrame as a horizontal stacked bar chart
    fig, ax = plt.subplots()
    ax.barh(df['Category'], df['Values'])
    ax.set_xlabel('Values')
    ax.set_ylabel('Category')
    ax.set_title('Random Integer Values')
    plt.show()

    return fig, ax