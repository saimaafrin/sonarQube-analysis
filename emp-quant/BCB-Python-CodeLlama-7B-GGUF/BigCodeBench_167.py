
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def task_func(num_types=5, integer_range=(0, 100)):
    # Generate random data
    data = {
        'Category{}'.format(i): [randint(integer_range[0], integer_range[1]) for _ in range(num_types)]
        for i in range(num_types)
    }
    df = pd.DataFrame(data)

    # Visualize data as a horizontal stacked bar chart
    fig, ax = plt.subplots()
    ax.barh(df.index, df.values, color='#0072B1')
    ax.set_xlabel('Values')
    ax.set_ylabel('Categories')
    ax.set_title('Horizontal Stacked Bar Chart')
    ax.set_yticks(df.index)
    ax.set_yticklabels(df.index)
    ax.invert_yaxis()
    fig.tight_layout()

    return fig, ax