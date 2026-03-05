
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler

def task_func(data, column, outlier_z_score):
    # Standardize the column
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[:, column].reshape(-1, 1))

    # Calculate Z-scores
    z_scores = stats.zscore(scaled_data)

    # Identify outliers
    outliers = np.where(np.abs(z_scores) > outlier_z_score)[0]

    # Remove outliers
    clean_data = np.delete(scaled_data, outliers, axis=0)

    # Visualize data
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.scatter(scaled_data[:, 0], scaled_data[:, 1], c='blue', alpha=0.5)
    ax1.set_title('Data with Outliers')
    ax2.scatter(clean_data[:, 0], clean_data[:, 1], c='red', alpha=0.5)
    ax2.set_title('Data without Outliers')
    plt.show()

    # Return data without outliers and indices of outliers
    return clean_data, outliers

clean_data, outliers = task_func(data, column, outlier_z_score)
print(clean_data)
print(outliers)