
import numpy as np
import matplotlib.pyplot as plt

# Constants
ARRAY_SIZE = 10000

def task_func():
    # Generate random integers
    random_array = np.random.randint(1, 101, ARRAY_SIZE)
    
    # Calculate mean and standard deviation
    mean = np.mean(random_array)
    std_dev = np.std(random_array)
    
    # Create histogram
    fig, ax = plt.subplots()
    ax.hist(random_array, bins=50, density=True, alpha=0.6, color='g')
    
    # Plot mean and standard deviation
    ax.axvline(mean, color='r', linestyle='--', linewidth=2, label='Mean')
    ax.axvline(mean - std_dev, color='purple', linestyle='--', linewidth=2, label='Mean - Std Dev')
    ax.axvline(mean + std_dev, color='purple', linestyle='--', linewidth=2, label='Mean + Std Dev')
    
    # Set labels and title
    ax.set_xlabel('Val')
    ax.set_ylabel('Freq')
    ax.set_title('Histogram of Random Values')
    ax.legend()
    
    # Return the array, mean, standard deviation, and the histogram plot
    return random_array, mean, std_dev, ax