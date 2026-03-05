
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def task_func(num_rows=5, rand_range=(0, 100)):
    # Create a DataFrame with random integer values
    data = pd.DataFrame({
        'A': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'B': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'C': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'D': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'E': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)]
    })

    # Visualize the data with a stacked bar chart
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(data['A'], data['B'], data['C'], data['D'], data['E'])
    ax.set_xlabel('Value')
    ax.set_ylabel('Count')
    ax.set_title('Stacked Bar Chart')
    ax.set_xticks(ax.get_xticks()[::2])
    ax.set_xticklabels(ax.get_xticks()[::2])
    plt.show()

    return fig