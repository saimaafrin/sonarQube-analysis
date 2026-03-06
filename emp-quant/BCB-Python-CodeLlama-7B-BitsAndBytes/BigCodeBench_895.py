
import numpy as np
import matplotlib.pyplot as plt

# Constants
ARRAY_SIZE = 10000

def task_func():
    # Generate an array of random integers between 1 and 100
    arr = np.random.randint(1, 100, size=ARRAY_SIZE)

    # Calculate the mean and standard deviation of the array
    mean = np.mean(arr)
    std = np.std(arr)

    # Plot the histogram of the distribution
    fig, ax = plt.subplots()
    ax.hist(arr, bins=50, density=True, alpha=0.5, label='Histogram of Random Values')
    ax.set_xlabel('Val')
    ax.set_ylabel('Freq')
    ax.axvline(mean, color='red', linestyle='dashed', label='Mean')
    ax.axvline(mean + std, color='purple', linestyle='dashed', label='Standard Deviation')
    ax.legend()

    return (arr, mean, std, fig)

# Call the function and print the results
arr, mean, std, fig = task_func()
print(f'Array: {arr}')
print(f'Mean: {mean}')
print(f'Standard Deviation: {std}')
print(f'Histogram: {fig}')