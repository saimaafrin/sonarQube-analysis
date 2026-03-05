
import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

def task_func(intervals=100, seed=0):
    # Generate a series of random numbers over the specified intervals
    times = [time.time() for i in range(intervals)]
    random.seed(seed)
    numbers = [random.randint(0, 100) for i in range(intervals)]

    # Plot the numbers as a function of elapsed time
    fig, ax = plt.subplots()
    ax.plot(times, numbers)
    ax.set_xlabel("Elapsed Time")
    ax.set_ylabel("Random Number")
    ax.set_title("Random Numbers over Time")

    # Calculate the kurtosis of the generated numbers
    kurtosis_value = kurtosis(numbers)

    return ax, kurtosis_value