
import pandas as pd
import seaborn as sns

def task_func(data):
    # Check if the DataFrame is empty
    if data.empty:
        raise ValueError("The DataFrame is empty")

    # Get the numeric columns
    numeric_columns = data.select_dtypes(include=[np.number])

    # Create a heatmap of the cumulative sum of each column
    heatmap = sns.heatmap(numeric_columns.cumsum(), cmap="viridis")

    # Return the Axes object of the heatmap
    return heatmap