
import numpy as np
import matplotlib.pyplot as plt
# Constants
ARRAY_SIZE = 10000

def task_func():
    # Generate a numeric array of random integers
    random_array = np.random.randint(1, 101, ARRAY_SIZE)
    
    # Calculate the mean and standard deviation
    mean = np.mean(random_array)
    std_dev = np.std(random_array)
    
    # Create a histogram of the distribution
    fig, ax = plt.subplots()
    ax.hist(random_array, bins=30, edgecolor='k')
    ax.set_title('Histogram of Random Integers')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Plot the mean and standard deviation as dashed lines
    ax.axvline(mean, color='r', linestyle='--', label='Mean')
    ax.axvline(mean + std_dev, color='purple', linestyle='--', label='Mean + Std Dev')
    ax.axvline(mean - std_dev, color='purple', linestyle='--', label='Mean - Std Dev')
    
    # Return the array, mean, standard deviation, and the histogram plot
    return random_array, mean, std_dev, ax