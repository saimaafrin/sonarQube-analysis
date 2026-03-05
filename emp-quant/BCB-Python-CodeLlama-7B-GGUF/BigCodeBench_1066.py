
import numpy as np
import matplotlib.pyplot as plt

# Constants
NUM_SAMPLES = 100
NUM_OUTLIERS = 5

def task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    # Generate normally distributed data
    data = np.random.normal(size=num_samples)

    # Generate artificially introduced outliers
    outliers = np.random.normal(size=num_outliers) * 10

    # Combine data and outliers
    data = np.concatenate((data, outliers))

    # Detect outliers using IQR method
    outliers_detected = np.array([])
    for i in range(len(data)):
        if data[i] < np.percentile(data, 25) or data[i] > np.percentile(data, 75):
            outliers_detected = np.append(outliers_detected, data[i])

    # Plot histogram of combined data
    fig, ax = plt.subplots()
    ax.hist(data, bins=50)
    ax.set_title('Histogram of Combined Data')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    plt.show()

    return data, outliers_detected, ax

# Call function
data, outliers_detected, ax = task_func()