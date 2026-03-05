import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def task_func(data: pd.DataFrame) -> (pd.DataFrame, list):
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the data
    standardized_data = scaler.fit_transform(data)
    
    # Convert the standardized data back to a DataFrame
    standardized_data = pd.DataFrame(standardized_data, columns=data.columns)
    
    # Create a list to hold the Axes objects
    axes_list = []
    
    # Plot histograms for each feature
    fig, axes = plt.subplots(nrows=1, ncols=len(data.columns), figsize=(15, 3))
    
    for i, column in enumerate(data.columns):
        axes[i].hist(standardized_data[column], bins=20)
        axes[i].set_title(f'Histogram of {column}')
        axes_list.append(axes[i])
    
    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()
    
    return standardized_data, axes_list