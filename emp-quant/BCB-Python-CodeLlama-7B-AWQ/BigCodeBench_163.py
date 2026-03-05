import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(rows=5, cols=5):
    """
    Generates a DataFrame with random numerical data and visualizes this data in a stacked bar chart for specified categories.
    """
    # Generate random data
    data = np.random.randint(1, 100, size=(rows, cols))
    # Create DataFrame
    df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])
    # Create categories
    categories = ['A', 'B', 'C', 'D', 'E']
    # Check if number of columns exceeds number of available categories
    if len(df.columns) > len(categories):
        raise ValueError("ValueError: If the number of columns exceeds the number of available categories.")
    # Create stacked bar chart
    ax = df.plot(kind='bar', stacked=True, figsize=(10, 6), rot=0, legend=False)
    ax.set_title('Stacked Bar Chart')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(categories)
    return ax
rows = 5
cols = 5