
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
    ax.set_title('Histogram of Random Values')
    ax.set_xlabel('Val')
    ax.set_ylabel('Freq')
    
    # Plot the mean and standard deviation as dashed lines
    ax.axvline(mean, color='r', linestyle='--', label=f'Mean: {mean:.2f}')
    ax.axvline(mean + std_dev, color='purple', linestyle='--', label=f'Mean + Std Dev: {mean + std_dev:.2f}')
    ax.axvline(mean - std_dev, color='purple', linestyle='--', label=f'Mean - Std Dev: {mean - std_dev:.2f}')
    
    # Show the legend
    ax.legend()
    
    # Return the array, mean, standard deviation, and the histogram plot
    return random_array, mean, std_dev, ax