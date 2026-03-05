import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(a, b):
    # Generate random values for the DataFrame
    data = np.random.randint(1, 100, size=(len(a), len(b)))

    # Create a DataFrame with the random values
    df = pd.DataFrame(data, index=a, columns=b)

    # Plot the DataFrame as a bar chart
    ax = df.plot(kind='bar', rot=0, figsize=(10, 6))

    # Set the x-axis labels
    ax.set_xticklabels(df.index)

    # Set the y-axis labels
    ax.set_yticklabels(df.columns)

    # Return the Axes object of the plotted bar chart
    return ax
a = ['A', 'B', 'C', 'D', 'E']
b = [10, 20, 30, 40, 50]