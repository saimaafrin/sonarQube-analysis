import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler
def task_func(data, column, outlier_z_score):
    """
    Identifies and removes outliers from a specified column of a dataset based on the Z-score.
    It standardizes the column, calculates Z-scores, and removes data points where the Z-score exceeds a threshold.
    The function also visualizes the data before and after outlier removal.
    """
    # Standardize the column
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[:, column])

    # Calculate Z-scores
    z_scores = stats.zscore(scaled_data)

    # Identify outliers
    outliers = np.where(np.abs(z_scores) > outlier_z_score)[0]

    # Remove outliers
    data_without_outliers = np.delete(data, outliers, axis=0)

    # Visualize data
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.scatter(data[:, column], data[:, column], c='blue')
    ax1.set_title('Data with Outliers')
    ax2.scatter(data_without_outliers[:, column], data_without_outliers[:, column], c='red')
    ax2.set_title('Data without Outliers')
    plt.show()

    return data, data_without_outliers, outliers
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
column = 1
outlier_z_score = 2