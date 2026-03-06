
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(num_groups=5, data_size=5, labels=None):
    # Generate random data
    data = np.random.randint(0, 100, size=(num_groups, data_size))
    df = pd.DataFrame(data, columns=['Group {}'.format(i) for i in range(1, num_groups+1)])

    # Create a stacked bar chart
    fig, ax = plt.subplots()
    ax.bar(df.columns, df.sum(axis=1), color='#333333')
    ax.set_title('Stacked Bar Chart')
    ax.set_xlabel('Group')
    ax.set_ylabel('Value')
    ax.set_xticks(range(num_groups))
    ax.set_xticklabels(df.columns)
    ax.legend(loc='upper left')

    # Save the plot to a file
    fig.savefig('test_plot.png')

    return fig, df, 'test_plot.png'