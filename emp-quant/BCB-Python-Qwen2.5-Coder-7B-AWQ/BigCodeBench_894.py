import numpy as np
import matplotlib.pyplot as plt
ARRAY_SIZE = 10000
def task_func():
    # Generate a numeric array of random integers between 1 and 100
    random_array = np.random.randint(1, 101, ARRAY_SIZE)
    
    # Calculate the mean and standard deviation of the array
    mean = np.mean(random_array)
    std_dev = np.std(random_array)
    
    # Create a histogram of the distribution
    fig, ax = plt.subplots()
    ax.hist(random_array, bins=50, density=True, alpha=0.6, color='g')
    
    # Plot the mean as a red dashed line
    ax.axvline(mean, color='r', linestyle='--', linewidth=2, label=f'Mean: {mean:.2f}')
    
    # Plot the standard deviation as purple dashed lines
    ax.axvline(mean - std_dev, color='purple', linestyle='--', linewidth=2, label=f'Mean - Std Dev: {mean - std_dev:.2f}')
    ax.axvline(mean + std_dev, color='purple', linestyle='--', linewidth=2, label=f'Mean + Std Dev: {mean + std_dev:.2f}')
    
    # Set the title and labels
    ax.set_title('Histogram of Random Integers')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Add a legend
    ax.legend()
    
    # Return the array, mean, standard deviation, and the histogram plot
    return random_array, mean, std_dev, ax