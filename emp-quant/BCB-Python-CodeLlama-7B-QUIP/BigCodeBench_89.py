
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler

def task_func(data, column, outlier_z_score):
    # Standardize the column
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data[:, column].reshape(-1, 1))

    # Calculate Z-scores
    z_scores = stats.zscore(data_scaled)

    # Remove outliers
    outliers = np.abs(z_scores) > outlier_z_score
    data_without_outliers = data[~outliers]

    # Visualize the data before and after outlier removal
    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
    ax[0].scatter(data[:, column], data_scaled)
    ax[1].scatter(data_without_outliers[:, column], data_scaled[~outliers])
    plt.show()

    return data, data_without_outliers, outliers