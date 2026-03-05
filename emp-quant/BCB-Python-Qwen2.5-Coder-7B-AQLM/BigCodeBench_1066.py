
import numpy as np
import matplotlib.pyplot as plt

# Constants
NUM_SAMPLES = 100
NUM_OUTLIERS = 5

def task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    # Generate normally distributed data
    normal_data = np.random.normal(loc=0, scale=1, size=num_samples)
    
    # Generate artificially introduced outliers
    outlier_data = np.random.normal(loc=5, scale=2, size=num_outliers)
    
    # Combine the data
    data = np.concatenate((normal_data, outlier_data))
    
    # Sort the data to facilitate IQR calculation
    sorted_data = np.sort(data)
    
    # Calculate the IQR
    Q1 = np.percentile(sorted_data, 25)
    Q3 = np.percentile(sorted_data, 75)
    IQR = Q3 - Q1
    
    # Define the lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Detect outliers using IQR method
    outliers_detected = data[(data < lower_bound) | (data > upper_bound)]
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, color='blue', alpha=0.7)
    ax.set_title('Histogram of Combined Data')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Highlight the outliers
    ax.scatter(outliers_detected, np.zeros_like(outliers_detected), color='red', label='Outliers')
    ax.legend()
    
    return data, outliers_detected, ax