
import numpy as np
import matplotlib.pyplot as plt

def task_func():
    # Generate x values from 0 to 2*pi
    x = np.linspace(0, 2 * np.pi, 100)
    
    # Calculate sine and cosine values
    sin_values = np.sin(x)
    cos_values = np.cos(x)
    
    # Create a figure and two subplots
    fig, axs = plt.subplots(2, 1, figsize=(8, 6))
    
    # Plot the sine function
    axs[0].plot(x, sin_values, label='Sine function')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('sin(x)')
    axs[0].legend()
    
    # Plot the cosine function
    axs[1].plot(x, cos_values, label='Cosine function')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('cos(x)')
    axs[1].legend()
    
    return fig, axs