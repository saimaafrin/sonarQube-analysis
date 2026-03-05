
import pandas as pd
import seaborn as sns

def task_func(data):
    # Check if the DataFrame is empty
    if data.empty:
        raise ValueError("DataFrame is empty")

    # Check if there are any numeric columns
    if not data.select_dtypes(include=[np.number]).columns.size:
        raise ValueError("No numeric columns present")

    # Create a Seaborn heatmap of the cumulative sum of each column
    sns.heatmap(data.cumsum(), annot=True, cmap="YlGnBu")

    # Return the Axes object of the Seaborn heatmap
    return sns.heatmap(data.cumsum(), annot=True, cmap="YlGnBu").axes