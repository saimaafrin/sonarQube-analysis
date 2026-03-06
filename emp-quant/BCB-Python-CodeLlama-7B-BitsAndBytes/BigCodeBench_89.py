
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler

def task_func(data, column, outlier_z_score):
    # Standardize the column
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[column].values.reshape(-1, 1))

    # Calculate Z-scores
    z_scores = stats.zscore(scaled_data)

    # Identify outliers
    outliers = np.where(np.abs(z_scores) > outlier_z_score)[0]

    # Remove outliers
    data_without_outliers = np.delete(data, outliers, axis=0)

    # Plot data before and after outlier removal
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.scatter(data[column], data[column], label='Data with Outliers')
    ax1.set_title('Original Data')
    ax1.set_xlabel(column)
    ax1.set_ylabel(column)
    ax1.legend()

    ax2.scatter(data_without_outliers[column], data_without_outliers[column], label='Data without Outliers')
    ax2.set_title('Data after Outlier Removal')
    ax2.set_xlabel(column)
    ax2.set_ylabel(column)
    ax2.legend()

    return (data, data_without_outliers, outliers)

# Call the function
result = task_func(data, 'A', outlier_z_score)

# Print the results
print(result)