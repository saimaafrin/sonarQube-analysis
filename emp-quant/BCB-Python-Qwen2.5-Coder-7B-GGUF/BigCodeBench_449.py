
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def task_func(data: pd.DataFrame) -> (pd.DataFrame, list):
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Standardize the data
    standardized_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
    
    # Create a figure and a list to hold the axes
    fig, axes_list = plt.subplots(nrows=standardized_data.shape[1], ncols=1, figsize=(8, 2*standardized_data.shape[1]))
    
    # Plot histograms for each feature
    for i, column in enumerate(standardized_data.columns):
        axes_list[i].hist(standardized_data[column], bins=20, edgecolor='black')
        axes_list[i].set_title(f'Histogram of {column}')
        axes_list[i].set_xlabel('Value')
        axes_list[i].set_ylabel('Frequency')
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    # Return the standardized data and the list of axes
    return standardized_data, axes_list