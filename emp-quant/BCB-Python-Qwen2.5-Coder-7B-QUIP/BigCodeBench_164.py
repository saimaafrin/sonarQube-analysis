
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(num_labels=5, data_range=(0, 1)):
    # Generate random data for each label
    labels = [f"Label {i+1}" for i in range(num_labels)]
    data = np.random.randint(data_range[0], data_range[1], size=(num_labels, 3))
    
    # Create a DataFrame to hold the data
    df = pd.DataFrame(data, columns=labels)
    
    # Create a stacked bar chart
    fig, ax = plt.subplots()
    ax.bar(range(3), df.sum(axis=0), label='Total')
    ax.set_xlabel('Data Points')
    ax.set_ylabel('Values')
    ax.set_title('Stacked Bar Chart')
    ax.legend()
    
    return fig