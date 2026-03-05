
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

def task_func(data: pd.DataFrame) -> (pd.DataFrame, plt.Axes):
    # Normalize the data
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)

    # Create a heatmap of the normalized data
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(normalized_data, cmap="YlGnBu", annot=True, ax=ax, cbar_kws={"label": "Normalized Value"})

    return normalized_data, ax