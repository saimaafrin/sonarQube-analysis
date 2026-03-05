
import numpy as np
import matplotlib.pyplot as plt

# Constants
NUM_SAMPLES = 100
NUM_OUTLIERS = 5

def task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    # Generate normally distributed data
    mean = 0
    std = 1
    normal_data = np.random.normal(mean, std, num_samples)
    
    # Introduce artificially introduced outliers
    outliers = np.random.uniform(-10, 10, num_outliers)
    data = np.concatenate([normal_data, outliers])
    
    # Detect outliers using IQR method
    Q1 = np.percentile(normal_data, 25)
    Q3 = np.percentile(normal_data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers_detected = np.array([x for x in data if x < lower_bound or x > upper_bound])
    
    # Plot histogram of the combined dataset
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, color='k', edgecolor='k')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Combined Dataset')
    
    return data, outliers_detected, ax