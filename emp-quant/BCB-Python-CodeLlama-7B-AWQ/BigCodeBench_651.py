import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def task_func(df, target_value):
    """
    Convert the input dic of list to DataFrame and searcher in this DataFrame for rows with cells equal to the provided target_value. It then plots the count of such rows per column.
    The function should output with:
        tuple: A tuple containing:
        A pandas Series with counts of the target value per column.
        A matplotlib Axes object representing the plot (None if dataframe is empty).
    """
    # Convert the input dic of list to DataFrame
    df = pd.DataFrame(df)

    # Search for rows with cells equal to the provided target_value
    target_rows = df[df == target_value]

    # Count the number of rows with cells equal to the provided target_value per column
    counts = target_rows.count(axis=0)

    # Plot the count of such rows per column
    if not counts.empty:
        fig, ax = plt.subplots()
        counts.plot(kind='bar', ax=ax)
        ax.set_title('Count of rows with target value per column')
        ax.set_xlabel('Column')
        ax.set_ylabel('Count')
        return counts, ax
    else:
        return counts, None
df = {}
target_value = 1