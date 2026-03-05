
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def task_func(array_length=100, noise_level=0.2):
    # Generate time points
    t = np.linspace(0, 1, array_length)
    
    # Generate a noisy sine wave
    sine_wave = np.sin(2 * np.pi * t) + noise_level * np.random.normal(size=array_length)
    
    # Define the sine function to fit
    def sine_func(x, amplitude, frequency, phase, offset):
        return amplitude * np.sin(2 * np.pi * frequency * x + phase) + offset
    
    # Initial guess for the parameters
    p0 = [1, 1, 0, 0]
    
    # Perform curve fitting
    params, covariance = curve_fit(sine_func, t, sine_wave, p0=p0)
    
    # Extract the fitted parameters
    amplitude_fit, frequency_fit, phase_fit, offset_fit = params
    
    # Generate the fitted sine wave
    sine_fit = sine_func(t, amplitude_fit, frequency_fit, phase_fit, offset_fit)
    
    # Plot the original noisy sine wave and the fitted curve
    fig, ax = plt.subplots()
    ax.plot(t, sine_wave, label='Noisy Sine Wave')
    ax.plot(t, sine_fit, label='Fitted Curve', color='red')
    ax.legend()
    plt.show()
    
    return ax