import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
FEATURE_NAMES = ["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5"]
def task_func(data_matrix):
    """
    Standardize a 2D data matrix, calculate the mean value of each row and then visualize the distribution of the mean values with an histogram.
    
    Parameters:
    data_matrix (np.ndarray): A 2D numpy array where each row represents a data point.
    
    Returns:
    tuple: A tuple containing:
        pandas.DataFrame: A DataFrame containing the standardized data and the mean of each row.
        Its column names should be FEATURE_NAMES and 'Mean'.
        matplotlib.axes.Axes: The histogram plot of the distribution of means.
    """
    # Standardize the data
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data_matrix)
    
    # Calculate the mean of each row
    row_means = standardized_data.mean(axis=1)
    
    # Create a DataFrame to store the standardized data and the means
    result_df = pd.DataFrame(standardized_data, columns=FEATURE_NAMES)
    result_df['Mean'] = row_means
    
    # Plot the distribution of means
    fig, ax = plt.subplots()
    ax.hist(row_means, bins=10, color='blue', edgecolor='black')
    ax.set_title('Distribution of Means')
    ax.set_xlabel('Mean Value')
    ax.set_ylabel('Frequency')
    
    return result_df, ax