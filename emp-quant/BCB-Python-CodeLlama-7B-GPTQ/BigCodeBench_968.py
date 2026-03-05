import pandas as pd
import seaborn as sns
def task_func(data):
    """
    Creates and returns a heatmap of the cumulative sum of each column in a dictionary.
    """
    # Check if the DataFrame is empty
    if data.empty:
        raise ValueError("DataFrame is empty")

    # Check if there are any numeric columns
    if not data.select_dtypes(include=[np.number]).columns.size:
        raise ValueError("No numeric columns present")

    # Create a new DataFrame with the cumulative sum of each column
    cumulative_sum = data.cumsum()

    # Create a Seaborn heatmap of the cumulative sum
    ax = sns.heatmap(cumulative_sum, annot=True, cmap="Blues")

    return ax
data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})