
import numpy as np
import matplotlib.pyplot as plt

# Constants
ARRAY_SIZE = 10000

def task_func():
    # Generate random integers
    data = np.random.randint(1, 101, ARRAY_SIZE)
    
    # Calculate mean and standard deviation
    mean = np.mean(data)
    std_dev = np.std(data)
    
    # Create histogram
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(data, bins=50, density=True, alpha=0.6, color='g')
    
    # Plot mean and standard deviation
    ax.axvline(mean, color='r', linestyle='--', linewidth=2, label=f'Mean: {mean:.2f}')
    ax.axvline(mean - std_dev, color='purple', linestyle='--', linewidth=2, label=f'Std Dev (-): {std_dev:.2f}')
    ax.axvline(mean + std_dev, color='purple', linestyle='--', linewidth=2, label=f'Std Dev (+): {std_dev:.2f}')
    
    # Set labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Random Integers')
    ax.legend()
    
    return data, mean, std_dev, ax