
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def task_func(mu, sigma, seed=0):
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate 1000 samples from a normal distribution
    samples = np.random.normal(mu, sigma, 1000)
    
    # Create a figure and an axes object
    fig, ax = plt.subplots()
    
    # Plot the normal distribution
    sns.kdeplot(samples, color='b', label='Density')
    
    # Add a color bar to indicate the density
    ax.set_title(f'Normal Distribution with μ={mu} and σ={sigma}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    
    # Return the axes object
    return ax