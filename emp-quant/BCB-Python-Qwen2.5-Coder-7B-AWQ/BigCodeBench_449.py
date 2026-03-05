import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def task_func(data: pd.DataFrame) -> (pd.DataFrame, list):
    """
    Standardizes the features of a pandas DataFrame and plots histograms for each feature.

    Parameters:
    data (pd.DataFrame): The input DataFrame with features to be standardized.

    Returns:
    standardized_data (pd.DataFrame): The DataFrame with standardized features.
    axes_list (list): A list of matplotlib Axes objects representing the histograms for each feature.
    """
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Standardize the data
    standardized_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
    
    # Create a list to hold the Axes objects
    axes_list = []
    
    # Plot histograms for each feature
    fig, axes = plt.subplots(nrows=1, ncols=len(data.columns), figsize=(20, 5))
    if len(data.columns) == 1:
        axes = [axes]
    for i, column in enumerate(data.columns):
        axes_list.append(axes[i])
        axes[i].hist(standardized_data[column], bins=20, edgecolor='black')
        axes[i].set_title(f'Histogram of {column}')
        axes[i].set_xlabel('Value')
        axes[i].set_ylabel('Frequency')
    
    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()
    
    return standardized_data, axes_list