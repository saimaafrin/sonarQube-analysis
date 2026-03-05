import numpy as np
import matplotlib.pyplot as plt
NUM_SAMPLES = 100
NUM_OUTLIERS = 5
def task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    # Generate normally distributed data
    data = np.random.normal(size=num_samples)

    # Introduce artificial outliers
    outliers = np.random.normal(size=num_outliers)
    outliers = outliers * 10
    data = np.concatenate((data, outliers))

    # Detect outliers using IQR method
    iqr = np.subtract(np.percentile(data, 75), np.percentile(data, 25))
    outliers_detected = data[np.abs(data - np.mean(data)) > iqr]

    # Plot histogram
    fig, ax = plt.subplots()
    ax.hist(data, bins=50)
    ax.set_title('Histogram of Combined Data')
    ax.set_xlabel('Data')
    ax.set_ylabel('Frequency')

    return data, outliers_detected, ax