
import pandas as pd
import seaborn as sns

def task_func(data):
    # Check if the DataFrame is empty
    if data.empty:
        raise ValueError("DataFrame is empty")

    # Check if there are any numeric columns
    if not data.select_dtypes(include=[np.number]).columns.size:
        raise ValueError("No numeric columns present")

    # Create a new DataFrame with the cumulative sum of each column
    cumulative_sum_data = data.cumsum(axis=1)

    # Create a Seaborn heatmap of the cumulative sum DataFrame
    ax = sns.heatmap(cumulative_sum_data, annot=True, cmap="YlGnBu")

    return ax