
import numpy as np
import matplotlib.pyplot as plt

# Constants
NUM_SAMPLES = 100
NUM_OUTLIERS = 5

def task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    # Generate normally distributed data
    data = np.random.normal(0, 1, num_samples)

    # Generate artificially introduced outliers
    outliers = np.random.normal(10, 1, num_outliers)

    # Combine data and outliers
    data = np.concatenate((data, outliers))

    # Detect outliers using IQR method
    outliers_detected = np.array(data[np.abs(data - np.median(data)) > 1.5 * np.std(data)])

    # Plot histogram of combined data
    fig, ax = plt.subplots()
    ax.hist(data, bins=50)
    ax.set_xlabel("Data")
    ax.set_ylabel("Count")
    ax.set_title("Histogram of Combined Data")
    plt.show()

    return data, outliers_detected, ax

# Run the function
data, outliers_detected, ax = task_func()