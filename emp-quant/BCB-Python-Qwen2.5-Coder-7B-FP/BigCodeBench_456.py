import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
def task_func(data: pd.DataFrame) -> (pd.DataFrame, plt.Axes):
    """
    Normalize the data and visualize it using a heatmap.
    
    Parameters:
    - data: pandas DataFrame to be normalized and visualized.
    
    Returns:
    - pd.DataFrame: Normalized data.
    - plt.Axes: Heatmap plot of the normalized data.
    """
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    normalized_data = scaler.fit_transform(data)
    
    # Convert the normalized data back to a DataFrame
    normalized_df = pd.DataFrame(normalized_data, columns=data.columns, index=data.index)
    
    # Create a heatmap plot
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(normalized_df, cmap="YlGnBu", cbar_kws={"label": "Normalized Value"})
    
    return normalized_df, heatmap