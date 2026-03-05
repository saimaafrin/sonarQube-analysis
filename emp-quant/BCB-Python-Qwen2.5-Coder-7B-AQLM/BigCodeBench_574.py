
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def task_func(array_length=100, noise_level=0.2):
    # Generate a time array
    t = np.linspace(0, 10, array_length)
    
    # Generate a sine wave
    sine_wave = np.sin(t)
    
    # Add noise to the sine wave
    noisy_sine_wave = sine_wave + noise_level * np.random.normal(size=array_length)
    
    # Define the sine function to fit
    def sine_func(x, amplitude, frequency, phase):
        return amplitude * np.sin(frequency * x + phase)
    
    # Initial guess for the parameters
    p0 = [1, 1, 0]
    
    # Fit the curve to the noisy data
    params, covariance = curve_fit(sine_func, t, noisy_sine_wave, p0=p0)
    
    # Create a plot
    fig, ax = plt.subplots()
    
    # Plot the original noisy sine wave
    ax.plot(t, noisy_sine_wave, label='Noisy Sine Wave')
    
    # Plot the fitted sine curve
    ax.plot(t, sine_func(t, *params), label='Fitted Curve', linestyle='--')
    
    # Add labels and legend
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return ax