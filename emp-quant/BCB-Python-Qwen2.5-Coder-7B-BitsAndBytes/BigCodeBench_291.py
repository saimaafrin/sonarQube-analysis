
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def task_func(mu, sigma, seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate 1000 samples from a normal distribution
    samples = np.random.normal(mu, sigma, 1000)
    
    # Create a figure and an axes object
    fig, ax = plt.subplots()
    
    # Plot the histogram of the samples
    sns.histplot(samples, kde=False, ax=ax, bins=30, color='blue')
    
    # Draw a vertical line at the mean
    ax.axvline(mu, color='red', linestyle='--', label=f'Mean ({mu})')
    
    # Calculate the standard deviation range
    std_range = (mu - sigma, mu + sigma)
    
    # Draw a vertical line at one standard deviation below the mean
    ax.axvline(std_range[0], color='green', linestyle=':', label=f'1 Std Dev Below Mean ({std_range[0]})')
    
    # Draw a vertical line at one standard deviation above the mean
    ax.axvline(std_range[1], color='green', linestyle=':', label=f'1 Std Dev Above Mean ({std_range[1]})')
    
    # Add a legend to the plot
    ax.legend()
    
    # Return the Axes object
    return ax