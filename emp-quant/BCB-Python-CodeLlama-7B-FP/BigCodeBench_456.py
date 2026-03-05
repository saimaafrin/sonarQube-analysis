import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
def task_func(data: pd.DataFrame) -> (pd.DataFrame, plt.Axes):
    """
    Normalize the data and visualize it using a heatmap.

    Args:
        data (pd.DataFrame): The data to be normalized and visualized.

    Returns:
        pd.DataFrame: Normalized data.
        plt.Axes: Heatmap plot of the normalized data.
    """
    # Normalize the data
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)

    # Visualize the normalized data using a heatmap
    sns.heatmap(normalized_data, cmap="YlGnBu", annot=True, cbar_kws={"label": "Normalized Value"})

    # Return the normalized data and the heatmap plot
    return normalized_data, sns.heatmap
data = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [2, 4, 6, 8, 10]})