
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
    ax.hist(arr, bins=50, edgecolor='black')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Random Integers')

    # Plot the mean and standard deviation as red and purple dashed lines
    ax.plot(mean, np.zeros(1), 'r--')
    ax.plot(std, np.zeros(1), 'purple--')

    # Return the tuple containing the array, mean, standard deviation, and the histogram plot
    return (arr, mean, std, fig)

# Call the function and print the output
arr, mean, std, fig = task_func()
print(f'Array: {arr}')
print(f'Mean: {mean}')
print(f'Standard Deviation: {std}')
print(f'Histogram Plot: {fig}')