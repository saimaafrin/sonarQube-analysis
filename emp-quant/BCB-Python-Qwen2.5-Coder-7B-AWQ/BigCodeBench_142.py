import numpy as np
import matplotlib.pyplot as plt
def task_func():
    # Generate x values from 0 to 2*pi
    x = np.linspace(0, 2 * np.pi, 100)
    
    # Calculate sine and cosine values
    sine_values = np.sin(x)
    cosine_values = np.cos(x)
    
    # Create a figure and a set of subplots
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    
    # Plot sine function
    axs[0].plot(x, sine_values, label='Sine function')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('sin(x)')
    axs[0].legend()
    
    # Plot cosine function
    axs[1].plot(x, cosine_values, label='Cosine function')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('cos(x)')
    axs[1].legend()
    
    # Return the figure and axes
    return fig, axs