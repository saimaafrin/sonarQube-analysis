
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(num_labels=5, data_range=(0, 1)):
    # Generate random numeric data across the specified range
    data = np.random.randint(data_range[0], data_range[1], size=(num_labels,))

    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['Label {}'.format(i) for i in range(1, num_labels+1)])

    # Create a stacked bar chart
    fig, ax = plt.subplots()
    ax.bar(df.index, df.values, color='#3399ff')
    ax.set_title('Stacked Bar Chart')
    ax.set_xlabel('Label')
    ax.set_ylabel('Value')
    ax.set_xticks(df.index)
    ax.set_xticklabels(df.columns)
    ax.legend()

    return fig