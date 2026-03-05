
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(num_groups=5, data_size=5, labels=None):
    # Generate random data
    data = np.random.randint(1, 10, size=(num_groups, data_size))
    # Create a DataFrame
    df = pd.DataFrame(data)
    # Create a stacked bar chart
    fig, ax = plt.subplots()
    ax.bar(df.index, df.values, label=labels)
    ax.set_ylabel("Count")
    ax.set_xlabel("Category")
    ax.set_title("Stacked Bar Chart")
    # Save the plot to a file
    fig.savefig("test_plot.png")
    return df, fig, "test_plot.png"