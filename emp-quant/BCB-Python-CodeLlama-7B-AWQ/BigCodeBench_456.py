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
    data_normalized = scaler.fit_transform(data)

    # Visualize the normalized data using a heatmap
    sns.set(style="white")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(data_normalized, cmap="YlGnBu", ax=ax, cbar_kws={"label": "Normalized Value"})

    return data_normalized, ax
data = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [2, 4, 6, 8, 10]})