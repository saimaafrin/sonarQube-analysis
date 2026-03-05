from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
def task_func(array_length=100, noise_level=0.2):
    # Generate a time array
    time = np.linspace(0, 10, array_length)
    
    # Generate a noisy sine wave
    sine_wave = np.sin(time) + noise_level * np.random.normal(size=array_length)
    
    # Define the sine function to fit
    def sine_func(x, amplitude, frequency, phase):
        return amplitude * np.sin(2 * np.pi * frequency * x + phase)
    
    # Initial guess for the parameters
    p0 = [1, 1, 0]
    
    # Perform curve fitting
    params, covariance = curve_fit(sine_func, time, sine_wave, p0=p0)
    
    # Extract the fitted parameters
    amplitude, frequency, phase = params
    
    # Generate the fitted sine wave
    fitted_sine_wave = sine_func(time, amplitude, frequency, phase)
    
    # Plot the original noisy sine wave and the fitted curve
    fig, ax = plt.subplots()
    ax.plot(time, sine_wave, label='Noisy Sine Wave')
    ax.plot(time, fitted_sine_wave, label='Fitted Curve', color='red')
    ax.legend()
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Noisy Sine Wave and Fitted Curve')
    
    return ax