
import numpy as np
import matplotlib.pyplot as plt

# Constants
NUM_SAMPLES = 100
NUM_OUTLIERS = 5

def task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    # Generate normally distributed data
    data = np.random.normal(size=num_samples)

    # Generate artificially introduced outliers
    outliers = np.random.normal(size=num_outliers)
    outliers = outliers * 10

    # Combine data and outliers
    data = np.concatenate((data, outliers))

    # Detect outliers using IQR method
    outliers_detected = np.array([])
    for i in range(len(data)):
        if data[i] < data[i] - 1.5 * np.interquartile_range(data) or data[i] > data[i] + 1.5 * np.interquartile_range(data):
            outliers_detected = np.append(outliers_detected, data[i])

    # Plot histogram of combined data
    fig, ax = plt.subplots()
    ax.hist(data, bins=50)
    ax.set_title('Histogram of Combined Data')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_xticks(np.arange(min(data), max(data), 1))
    ax.set_yticks(np.arange(0, len(data), 1))
    ax.set_xticklabels(np.arange(min(data), max(data), 1))
    ax.set_yticklabels(np.arange(0, len(data), 1))

    # Plot outliers detected using IQR method
    ax.scatter(outliers_detected, np.zeros(len(outliers_detected)), c='red', marker='o')

    return data, outliers_detected, ax

# Call the function
data, outliers_detected, ax = task_func()

# Print the outliers detected using IQR method
print('Outliers detected using IQR method:', outliers_detected)

# Show the plot
plt.show()