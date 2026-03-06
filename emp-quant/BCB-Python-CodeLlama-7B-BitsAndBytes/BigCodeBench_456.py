
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

def task_func(data: pd.DataFrame) -> (pd.DataFrame, plt.Axes):
    # Normalize the data
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)

    # Visualize the normalized data using a heatmap
    sns.heatmap(normalized_data, cmap="YlGnBu", annot=True, cbar_kws={"label": "Normalized Value"})

    # Return both the normalized data and the heatmap plot
    return normalized_data, plt.gca()