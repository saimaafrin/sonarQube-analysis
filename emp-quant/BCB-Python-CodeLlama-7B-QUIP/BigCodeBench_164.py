
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(num_labels, data_range):
    # Generate random data
    data = np.random.randint(data_range[0], data_range[1], size=num_labels)
    # Create a pandas DataFrame
    df = pd.DataFrame(data)
    # Visualize the data with a stacked bar chart
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(df.index, df.values, label=df.index)
    ax.set_xlabel("Labels")
    ax.set_ylabel("Data")
    ax.set_title("Stacked Bar Chart")
    fig.show()
    return fig