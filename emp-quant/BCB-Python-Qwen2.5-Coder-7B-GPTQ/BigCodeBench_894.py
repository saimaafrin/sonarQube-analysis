import numpy as np
import matplotlib.pyplot as plt
ARRAY_SIZE = 10000
def task_func():
    # Generate random integers between 1 and 100
    random_array = np.random.randint(1, 101, ARRAY_SIZE)
    
    # Calculate mean and standard deviation
    mean = np.mean(random_array)
    std_dev = np.std(random_array)
    
    # Create histogram
    fig, ax = plt.subplots()
    ax.hist(random_array, bins=50, color='blue', edgecolor='black')
    
    # Plot mean and standard deviation lines
    ax.axvline(mean, color='red', linestyle='--', label=f'Mean: {mean:.2f}')
    ax.axvline(mean - std_dev, color='purple', linestyle='--', label=f'Mean - Std Dev: {mean - std_dev:.2f}')
    ax.axvline(mean + std_dev, color='purple', linestyle='--', label=f'Mean + Std Dev: {mean + std_dev:.2f}')
    
    # Set labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Random Integers')
    ax.legend()
    
    # Return the array, mean, standard deviation, and the histogram plot
    return random_array, mean, std_dev, ax