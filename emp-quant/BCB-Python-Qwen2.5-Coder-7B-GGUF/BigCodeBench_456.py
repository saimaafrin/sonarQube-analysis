
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

def task_func(data: pd.DataFrame) -> (pd.DataFrame, plt.Axes):
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    normalized_data = scaler.fit_transform(data)
    
    # Convert the normalized data back to a DataFrame
    normalized_df = pd.DataFrame(normalized_data, columns=data.columns, index=data.index)
    
    # Create a heatmap of the normalized data
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(normalized_df, cmap="YlGnBu", cbar_kws={"label": "Normalized Value"})
    
    # Return the normalized DataFrame and the heatmap plot
    return normalized_df, heatmap