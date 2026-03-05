
import numpy as np
import matplotlib.pyplot as plt

# Constants
NUM_SAMPLES = 100
NUM_OUTLIERS = 5

def task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    """
    Generates a dataset with both normal data and artificially introduced outliers,
    plots a histogram of the combined data, and detects outliers using the IQR method.
    
    Parameters:
    num_samples (int): Number of normally distributed samples.
    num_outliers (int): Number of artificially introduced outliers.
    
    Returns:
    data (numpy array): The combined dataset.
    outliers_detected (numpy array): The outliers detected using the IQR method.
    ax (matplotlib.axes._axes.Axes): The Axes object for the histogram plot.
    """
    # Generate normally distributed data
    normal_data = np.random.normal(0, 1, num_samples)
    
    # Generate artificially introduced outliers
    outlier_data = np.random.uniform(-10, 10, num_outliers)
    
    # Combine data
    data = np.concatenate((normal_data, outlier_data))
    
    # Plot histogram
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, color='blue', alpha=0.7)
    ax.set_title('Histogram of Combined Data')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Detect outliers using IQR method
    Q1 = np.percentile(normal_data, 25)
    Q3 = np.percentile(normal_data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers_detected = data[(data < lower_bound) | (data > upper_bound)]
    
    return data, outliers_detected, ax