import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler
def task_func(data, column, outlier_z_score):
    # Standardize the column
    scaler = StandardScaler()
    data[column] = scaler.fit_transform(data[column].values.reshape(-1, 1))

    # Calculate Z-scores
    z_scores = stats.zscore(data[column])

    # Identify outliers
    outliers = np.abs(z_scores) > outlier_z_score

    # Remove outliers
    data = data[~outliers]

    # Visualize the data
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.scatter(data[column], data[column], c='blue', label='Data with Outliers')
    ax2.scatter(data[column], data[column], c='red', label='Data without Outliers')
    ax1.set_title('Original Data')
    ax2.set_title('Data after Outlier Removal')
    ax1.legend()
    ax2.legend()
    plt.show()

    # Return the original data, the data without outliers, and the indices of the outliers
    return data, data[~outliers], outliers.index
data = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                     'B': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]})
outlier_z_score = 2