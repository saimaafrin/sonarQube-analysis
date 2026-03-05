
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

def task_func(data: pd.DataFrame) -> (pd.DataFrame, plt.Axes):
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Normalize the data
    normalized_data = scaler.fit_transform(data)
    
    # Convert the normalized data back to a DataFrame
    normalized_df = pd.DataFrame(normalized_data, columns=data.columns)
    
    # Create the heatmap
    fig, ax = plt.subplots()
    heatmap = sns.heatmap(normalized_df, cmap="YlGnBu", ax=ax)
    
    # Add a color bar
    cbar = ax.figure.colorbar(heatmap, ax=ax, label="Normalized Value")
    
    # Return the normalized data and the heatmap plot
    return normalized_df, ax