import numpy as np
import matplotlib.pyplot as plt
ARRAY_SIZE = 10000
def task_func():
    # Generate a numeric array of random integers between 1 and 100
    random_array = np.random.randint(1, 101, ARRAY_SIZE)
    
    # Calculate the mean and standard deviation of the array
    mean_value = np.mean(random_array)
    std_deviation = np.std(random_array)
    
    # Create a histogram of the distribution
    fig, ax = plt.subplots()
    ax.hist(random_array, bins=50, density=True, alpha=0.6, color='g')
    
    # Plot the mean as a red dashed line
    ax.axvline(mean_value, color='r', linestyle='--', linewidth=2, label=f'Mean: {mean_value:.2f}')
    
    # Plot the standard deviation as purple dashed lines
    ax.axvline(mean_value - std_deviation, color='purple', linestyle='--', linewidth=2, label=f'Mean - Std Dev: {mean_value - std_deviation:.2f}')
    ax.axvline(mean_value + std_deviation, color='purple', linestyle='--', linewidth=2, label=f'Mean + Std Dev: {mean_value + std_deviation:.2f}')
    
    # Set the title and labels for the histogram
    ax.set_title('Histogram of Random Integers')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Add a legend to the plot
    ax.legend()
    
    # Return the array, mean, standard deviation, and the histogram plot
    return random_array, mean_value, std_deviation, ax