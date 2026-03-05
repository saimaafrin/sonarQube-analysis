
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Constants
FEATURE_NAMES = ["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5"]

def task_func(data_matrix):
    """
    Standardize a 2D data matrix, calculate the mean value of each row and then visualize the distribution of the mean values with an histogram.
    
    Parameters:
    data_matrix (numpy.ndarray): A 2D numpy array where each row represents a data point.
    
    Returns:
    tuple: A tuple containing:
    pandas.DataFrame: A DataFrame containing the standardized data and the mean of each row.
    Its column names should be FEATURE_NAMES and 'Mean'.
    matplotlib.axes.Axes: The histogram plot of the distribution of means.
    """
    # Standardize the data matrix
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data_matrix)
    
    # Calculate the mean of each row
    means = standardized_data.mean(axis=1)
    
    # Create a DataFrame with the standardized data and the means
    df = pd.DataFrame(standardized_data, columns=FEATURE_NAMES)
    df['Mean'] = means
    
    # Plot the distribution of means
    fig, ax = plt.subplots()
    ax.hist(means, bins=30, edgecolor='black')
    ax.set_title('Distribution of Means')
    ax.set_xlabel('Mean Value')
    ax.set_ylabel('Frequency')
    
    return df, ax