
import numpy as np
import matplotlib.pyplot as plt

# Constants
ARRAY_SIZE = 10000

def task_func():
    # Generate an array of random integers between 1 and 100
    array = np.random.randint(1, 100, size=ARRAY_SIZE)

    # Calculate the mean and standard deviation
    mean = np.mean(array)
    std = np.std(array)

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(array, bins=50, facecolor='blue', alpha=0.5)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of Random Integers")
    ax.plot(mean, 'r--')
    ax.plot(std, 'purple--')
    plt.show()

    return (array, mean, std, fig)