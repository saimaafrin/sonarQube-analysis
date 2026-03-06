
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def task_func(array_length=100, noise_level=0.2):
    # Generate time points
    x = np.linspace(0, 10, array_length)
    
    # Define the true sine function
    def sine_function(x, amplitude, frequency, phase):
        return amplitude * np.sin(frequency * x + phase)
    
    # True parameters for the sine wave
    true_amplitude = 2.0
    true_frequency = 3.0
    true_phase = 0.5
    
    # Generate noisy data
    y_true = sine_function(x, true_amplitude, true_frequency, true_phase)
    y_noisy = y_true + noise_level * np.random.normal(size=array_length)
    
    # Fit the noisy data to the sine function
    popt, pcov = curve_fit(sine_function, x, y_noisy)
    
    # Extract the optimized parameters
    fitted_amplitude, fitted_frequency, fitted_phase = popt
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the original noisy sine wave
    ax.plot(x, y_noisy, 'o', label='Noisy Data')
    
    # Plot the fitted sine wave
    ax.plot(x, sine_function(x, fitted_amplitude, fitted_frequency, fitted_phase), '-', label='Fitted Curve')
    
    # Add labels and legend
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return ax