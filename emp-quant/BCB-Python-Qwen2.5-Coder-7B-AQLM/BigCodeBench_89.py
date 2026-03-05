
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler

def task_func(data, column, outlier_z_score):
    """
    Identifies and removes outliers from a specified column of a dataset based on the Z-score.
    
    Parameters:
    - data: A pandas DataFrame containing the dataset.
    - column: The name of the column from which to remove outliers.
    - outlier_z_score: The Z-score threshold above which data points are considered outliers.
    
    Returns:
    - tuple: A tuple containing the original data, the data without outliers, and the indices of the outliers.
    """
    # Standardize the specified column
    scaler = StandardScaler()
    data[column] = scaler.fit_transform(data[[column]])
    
    # Calculate Z-scores for the specified column
    z_scores = np.abs(stats.zscore(data[column]))
    
    # Identify outliers
    outliers = np.where(z_scores > outlier_z_score)[0]
    
    # Remove outliers
    data_without_outliers = data.drop(outliers)
    
    # Plotting
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.scatter(range(len(data)), data[column], color='blue')
    plt.title('Data with Outliers')
    plt.xlabel('Index')
    plt.ylabel(column)
    
    plt.subplot(1, 2, 2)
    plt.scatter(range(len(data_without_outliers)), data_without_outliers[column], color='green')
    plt.title('Data without Outliers')
    plt.xlabel('Index')
    plt.ylabel(column)
    
    plt.tight_layout()
    plt.show()
    
    return (data, data_without_outliers, outliers)