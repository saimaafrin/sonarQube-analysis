
import numpy as np
import matplotlib.pyplot as plt

# Constants
ARRAY_SIZE = 10000

def task_func():
    # Generate random integers between 1 and 100
    random_array = np.random.randint(1, 100, size=ARRAY_SIZE)

    # Calculate mean and standard deviation
    mean = np.mean(random_array)
    std_dev = np.std(random_array)

    # Plot histogram
    fig, ax = plt.subplots()
    ax.hist(random_array, bins=50, facecolor='blue', alpha=0.5)
    ax.set_xlabel("Val")
    ax.set_ylabel("Freq")
    ax.set_title("Histogram of Random Values")
    ax.plot(mean, 'r--')
    ax.plot(std_dev, 'purple--')
    plt.show()

    return (random_array, mean, std_dev, fig)