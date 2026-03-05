import numpy as np
import matplotlib.pyplot as plt
NUM_SAMPLES = 100
NUM_OUTLIERS = 5
def task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    """
    Generate a dataset with both normal data and artificially introduced outliers,
    and plot a histogram of the combined data. Detect outliers using the IQR method
    on the normally distributed portion of the data.

    Parameters:
    num_samples (int): Number of normally distributed samples.
    num_outliers (int): Number of artificially introduced outliers.

    Returns:
    data (numpy array): Combined dataset including both normally distributed data and outliers.
    outliers_detected (numpy array): Outliers detected using the IQR method.
    ax (matplotlib.axes._axes.Axes): Axes object for the histogram plot.
    """
    # Generate normally distributed data
    normal_data = np.random.normal(loc=0, scale=1, size=num_samples)
    
    # Generate artificially introduced outliers
    outlier_data = np.random.normal(loc=5, scale=2, size=num_outliers)
    
    # Combine data
    data = np.concatenate((normal_data, outlier_data))
    
    # Detect outliers using IQR method on the normally distributed portion
    Q1 = np.percentile(normal_data, 25)
    Q3 = np.percentile(normal_data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers_detected = data[(data < lower_bound) | (data > upper_bound)]
    
    # Plot histogram
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, color='blue', alpha=0.7)
    ax.set_title('Histogram of Combined Data')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    return data, outliers_detected, ax