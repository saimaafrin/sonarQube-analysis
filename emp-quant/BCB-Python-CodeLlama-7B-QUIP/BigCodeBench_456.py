
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

def task_func(data: pd.DataFrame) -> (pd.DataFrame, plt.Axes):
    # Normalize the data to the range [0, 1]
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)

    # Create a heatmap plot of the normalized data
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(normalized_data, cmap="YlGnBu", ax=ax, cbar_ax=ax)
    cbar = ax.collections[0].colorbar
    cbar.set_label("Normalized Value")

    return normalized_data, fig