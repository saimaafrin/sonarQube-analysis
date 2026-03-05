import numpy as np
import matplotlib.pyplot as plt
NUM_SAMPLES = 100
NUM_OUTLIERS = 5
def task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    # Generate normally distributed data
    normal_data = np.random.normal(0, 1, num_samples)
    
    # Generate artificially introduced outliers
    outlier_data = np.random.uniform(-10, 10, num_outliers)
    
    # Combine data
    data = np.concatenate((normal_data, outlier_data))
    
    # Detect outliers using IQR method on the normally distributed portion
    Q1 = np.percentile(normal_data, 25)
    Q3 = np.percentile(normal_data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers_detected = normal_data[(normal_data < lower_bound) | (normal_data > upper_bound)]
    
    # Plot histogram of the combined dataset
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, color='blue', alpha=0.7)
    ax.set_title('Histogram of Combined Dataset')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    return data, outliers_detected, ax