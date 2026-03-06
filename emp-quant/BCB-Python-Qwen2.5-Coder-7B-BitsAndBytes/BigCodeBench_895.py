
import numpy as np
import matplotlib.pyplot as plt

# Constants
ARRAY_SIZE = 10000

def task_func():
    # Generate random integers
    data = np.random.randint(1, 101, ARRAY_SIZE)
    
    # Calculate mean and standard deviation
    mean_value = np.mean(data)
    std_deviation = np.std(data)
    
    # Create histogram
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(data, bins=50, density=True, alpha=0.6, color='g')
    
    # Plot mean and standard deviation
    ax.axvline(mean_value, color='r', linestyle='--', linewidth=2, label=f'Mean: {mean_value:.2f}')
    ax.axvline(mean_value - std_deviation, color='purple', linestyle='--', linewidth=2, label=f'Std Dev (-): {std_deviation:.2f}')
    ax.axvline(mean_value + std_deviation, color='purple', linestyle='--', linewidth=2, label=f'Std Dev (+): {std_deviation:.2f}')
    
    # Set labels and title
    ax.set_xlabel('Val')
    ax.set_ylabel('Freq')
    ax.set_title('Histogram of Random Values')
    ax.legend()
    
    return data, mean_value, std_deviation, ax