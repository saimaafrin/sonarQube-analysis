
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(rows=5, cols=5):
    # Generate random numerical data
    data = np.random.randint(0, 100, size=(rows, cols))

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Check if the number of columns exceeds the number of available categories
    if cols > rows:
        raise ValueError("Number of columns exceeds number of available categories")

    # Create a stacked bar chart
    ax = df.plot.bar(stacked=True)

    # Set the title and labels
    ax.set_title("Stacked Bar Chart")
    ax.set_xlabel("Categories")
    ax.set_ylabel("Values")

    # Return the Axes object
    return ax