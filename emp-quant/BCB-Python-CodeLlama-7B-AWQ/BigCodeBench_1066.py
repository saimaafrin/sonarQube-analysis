import numpy as np
import matplotlib.pyplot as plt
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
    iqr = np.subtract(np.percentile(data, 75), np.percentile(data, 25))
    outliers_detected = data[np.abs(data - np.mean(data)) > iqr * 1.5]

    # Plot histogram of combined data
    fig, ax = plt.subplots()
    ax.hist(data, bins=50, alpha=0.5, label='Combined data')
    ax.hist(outliers_detected, bins=50, alpha=0.5, label='Outliers detected')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.legend()
    plt.show()

    return data, outliers_detected, ax