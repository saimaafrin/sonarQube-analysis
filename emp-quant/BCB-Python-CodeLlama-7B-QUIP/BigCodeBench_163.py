
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(rows=5, cols=5):
    # Generate a DataFrame with random numerical data
    data = pd.DataFrame(np.random.rand(rows, cols))

    # Visualize the data in a stacked bar chart
    fig, ax = plt.subplots()
    ax.bar(data.columns, data.values, label=data.index)
    ax.set_title("Stacked Bar Chart")
    ax.set_xlabel("Categories")
    ax.set_ylabel("Values")
    ax.legend()
    return ax