import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
def task_func(data: pd.DataFrame) -> (pd.DataFrame, plt.Axes):
    # Normalize the data to a range [0, 1]
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)

    # Visualize the normalized data using a seaborn heatmap
    sns.heatmap(normalized_data, cmap="YlGnBu", annot=True, cbar_kws={"label": "Normalized Value"})

    # Return the normalized data and the heatmap plot
    return normalized_data, sns.heatmap
data = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})