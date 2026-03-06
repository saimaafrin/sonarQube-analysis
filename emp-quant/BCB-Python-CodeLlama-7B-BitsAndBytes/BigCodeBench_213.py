
import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

def task_func(intervals=100, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)

    # Generate a series of random numbers over the specified intervals
    x = [random.random() for _ in range(intervals)]

    # Plot the numbers as a function of elapsed time
    fig, ax = plt.subplots()
    ax.plot(x)

    # Calculate the kurtosis of the generated numbers
    kurtosis_value = kurtosis(x)

    # Return the Axes object and the kurtosis value
    return ax, kurtosis_value

# Call the function with the specified intervals and seed
ax, kurtosis_value = task_func(intervals=100, seed=0)

# Print the kurtosis value
print(f"Kurtosis value: {kurtosis_value}")

# Show the plot
plt.show()