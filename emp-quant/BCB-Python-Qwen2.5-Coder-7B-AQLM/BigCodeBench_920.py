
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data):
    """
    Draws and returns a correlation matrix heatmap for a DataFrame containing numerical columns.
    
    Parameters:
    data (pd.DataFrame): A DataFrame containing numerical columns.
    
    Returns:
    matplotlib.axes._axes.Axes: The matplotlib Axes object representing the heatmap.
    """
    # Calculate the correlation matrix
    correlation_matrix = data.corr()
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    
    # Set the title of the heatmap
    heatmap.set_title('Correlation Matrix')
    
    # Return the Axes object
    return heatmap