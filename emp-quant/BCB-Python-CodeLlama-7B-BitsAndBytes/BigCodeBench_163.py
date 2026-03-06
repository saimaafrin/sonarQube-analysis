
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(rows=5, cols=5):
    # Generate random numerical data
    data = np.random.randint(1, 100, size=(rows, cols))

    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])

    # Visualize the data in a stacked bar chart
    ax = df.plot(kind='bar', stacked=True, figsize=(10, 6))

    # Add a title and labels to the chart
    ax.set_title('Stacked Bar Chart')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')

    # Raise a ValueError if the number of columns exceeds the number of available categories
    if cols > len(df.columns):
        raise ValueError('Number of columns exceeds the number of available categories')

    return ax