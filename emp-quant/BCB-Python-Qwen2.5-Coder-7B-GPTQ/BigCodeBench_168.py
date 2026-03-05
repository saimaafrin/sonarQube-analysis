import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def task_func(num_groups=5, data_size=5, labels=None):
    # Generate random data
    if labels is None:
        labels = [f'Group {i+1}' for i in range(num_groups)]
    data = np.random.randint(1, 10, size=(data_size, num_groups))
    df = pd.DataFrame(data, columns=labels)
    
    # Create a stacked bar chart
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title('Stacked Bar Chart of Random Data')
    ax.set_xlabel('Data Points')
    ax.set_ylabel('Values')
    
    # Save the plot to a file
    filename = 'test_plot.png'
    plt.savefig(filename)
    
    return fig, df, filename