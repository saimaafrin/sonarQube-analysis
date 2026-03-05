import numpy as np
import matplotlib.pyplot as plt
ARRAY_SIZE = 10000
def task_func():
    # Generate random integers between 1 and 100
    random_array = np.random.randint(1, 101, ARRAY_SIZE)
    
    # Calculate mean and standard deviation
    mean_value = np.mean(random_array)
    std_dev = np.std(random_array)
    
    # Create histogram
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(random_array, bins=50, density=True, alpha=0.6, color='g')
    
    # Plot mean and standard deviation lines
    ax.axvline(mean_value, color='r', linestyle='--', linewidth=2, label=f'Mean: {mean_value:.2f}')
    ax.axvline(mean_value - std_dev, color='purple', linestyle='--', linewidth=2, label=f'Mean - Std Dev: {mean_value - std_dev:.2f}')
    ax.axvline(mean_value + std_dev, color='purple', linestyle='--', linewidth=2, label=f'Mean + Std Dev: {mean_value + std_dev:.2f}')
    
    # Set labels and title
    ax.set_xlabel('Val')
    ax.set_ylabel('Freq')
    ax.set_title('Histogram of Random Values')
    ax.legend()
    
    # Return the array, mean, standard deviation, and the histogram plot
    return random_array, mean_value, std_dev, ax