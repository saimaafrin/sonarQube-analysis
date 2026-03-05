import numpy as np
import matplotlib.pyplot as plt
NUM_SAMPLES = 100
NUM_OUTLIERS = 5
def task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    """
    Generate a dataset comprising both normal data and artificially introduced outliers,
    and plot a histogram of the combined data. The function detects outliers in the dataset
    using the Interquartile Range (IQR) method, but it only considers the normally distributed
    portion of the data for outlier detection.
    
    Parameters:
    - num_samples (int): Number of normally distributed samples.
    - num_outliers (int): Number of artificially introduced outliers.
    
    Returns:
    - data (numpy array): The combined dataset, including both normally distributed data and
      the artificially introduced outliers.
    - outliers_detected (numpy array): The outliers detected using the IQR method. This
      detection is based solely on the normally distributed portion of the data.
    - ax (matplotlib.axes._axes.Axes): The Axes object for the histogram plot of the combined dataset.
    """
    # Generate normally distributed data
    normal_data = np.random.normal(loc=0, scale=1, size=num_samples)
    
    # Generate artificially introduced outliers
    outlier_data = np.random.normal(loc=5, scale=2, size=num_outliers)
    
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
    
    # Identify outliers
    outliers_detected = data[(data < lower_bound) | (data > upper_bound)]
    
    return data, outliers_detected, ax