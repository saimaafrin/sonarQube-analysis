
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler

def task_func(data, column, outlier_z_score):
    """
    Identifies and removes outliers from a specified column of a dataset based on the Z-score.
    
    Parameters:
    data (pd.DataFrame): The input dataset.
    column (str): The column name to analyze for outliers.
    outlier_z_score (float): The Z-score threshold for identifying outliers.
    
    Returns:
    tuple: A tuple containing the original data, the data without outliers, and the indices of the outliers.
    """
    # Standardize the column
    scaler = StandardScaler()
    data[column] = scaler.fit_transform(data[column].values.reshape(-1, 1))
    
    # Calculate Z-scores
    z_scores = np.abs(stats.zscore(data[column]))
    
    # Identify outliers
    outliers = np.where(z_scores > outlier_z_score)[0]
    
    # Remove outliers
    data_cleaned = data.drop(outliers, axis=0)
    
    # Plotting
    plt.figure(figsize=(12, 6))
    
    # Plot original data with outliers
    plt.subplot(1, 2, 1)
    plt.scatter(range(len(data[column])), data[column], c='b', marker='o')
    plt.title('Data with Outliers')
    plt.xlabel('Index')
    plt.ylabel(column)
    
    # Plot data without outliers
    plt.subplot(1, 2, 2)
    plt.scatter(range(len(data_cleaned[column])), data_cleaned[column], c='r', marker='o')
    plt.title('Data without Outliers')
    plt.xlabel('Index')
    plt.ylabel(column)
    
    plt.tight_layout()
    plt.show()
    
    return (data, data_cleaned, outliers)