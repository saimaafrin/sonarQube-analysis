
import numpy as np
import matplotlib.pyplot as plt

# Constants
NUM_SAMPLES = 100
NUM_OUTLIERS = 5

def task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    # Generate normally distributed data
    normal_data = np.random.normal(0, 1, num_samples)
    
    # Introduce artificial outliers
    outlier_data = np.random.uniform(-3, 3, num_outliers)
    data = np.concatenate((normal_data, outlier_data))
    
    # Plot histogram of the combined data
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, color='blue', alpha=0.7)
    ax.set_title('Histogram of Combined Data')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Detect outliers using IQR method
    q1 = np.percentile(normal_data, 25)
    q3 = np.percentile(normal_data, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers_detected = normal_data[(normal_data < lower_bound) | (normal_data > upper_bound)]
    
    return data, outliers_detected, ax