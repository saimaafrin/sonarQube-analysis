
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

def task_func(data: pd.DataFrame) -> (pd.DataFrame, plt.Axes):
    """
    Normalize the data and visualize it using a heatmap.
    
    Parameters:
    data (pd.DataFrame): The input DataFrame to be normalized and visualized.
    
    Returns:
    pd.DataFrame: Normalized data.
    plt.Axes: Heatmap plot of the normalized data.
    """
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Normalize the data
    normalized_data = scaler.fit_transform(data)
    normalized_df = pd.DataFrame(normalized_data, columns=data.columns, index=data.index)
    
    # Create a heatmap plot
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(normalized_df, cmap="YlGnBu", annot=True, fmt=".2f", cbar_kws={"label": "Normalized Value"})
    
    # Return the normalized data and the heatmap plot
    return normalized_df, heatmap