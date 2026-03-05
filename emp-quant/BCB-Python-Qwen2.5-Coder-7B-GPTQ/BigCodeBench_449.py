import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def task_func(data: pd.DataFrame) -> (pd.DataFrame, list):
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Standardize the data
    standardized_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
    
    # Create a list to hold the Axes objects
    axes_list = []
    
    # Plot histograms for each feature
    fig, axes = plt.subplots(nrows=1, ncols=len(data.columns), figsize=(15, 3))
    for i, column in enumerate(data.columns):
        axes[i].hist(standardized_data[column], bins=20)
        axes[i].set_title(f'Histogram of {column}')
        axes[i].set_xlabel('Value')
        axes[i].set_ylabel('Frequency')
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    # Show the plot
    plt.show()
    
    # Return the standardized data and the list of Axes objects
    return standardized_data, axes_list