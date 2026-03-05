import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def task_func(num_groups=5, data_size=5, labels=None):
    """
    Generate random data and visualize it with a stacked bar chart, saving the chart to a file.
    This function facilitates the exploration and sharing of data distribution across multiple categories.
    """
    # Generate random data
    data = np.random.randint(0, 100, size=(num_groups, data_size))
    df = pd.DataFrame(data, columns=['Group {}'.format(i) for i in range(num_groups)])

    # Visualize data with a stacked bar chart
    fig, ax = plt.subplots()
    ax.bar(df.index, df.sum(axis=1), color='#333333')
    ax.set_title('Stacked Bar Chart')
    ax.set_xlabel('Group')
    ax.set_ylabel('Value')
    ax.set_xticks(df.index)
    ax.set_xticklabels(df.columns)
    ax.legend(loc='upper left')

    # Save plot to file
    fig.savefig('test_plot.png')

    return fig, df, 'test_plot.png'