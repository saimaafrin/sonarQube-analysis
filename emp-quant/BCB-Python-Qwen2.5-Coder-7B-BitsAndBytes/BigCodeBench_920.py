
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
    corr_matrix = data.corr()

    # Create a figure and axis for the plot
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)

    # Set the title of the heatmap
    ax.set_title('Correlation Matrix')

    # Return the Axes object
    return ax