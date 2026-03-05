from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
def task_func(array_length=100, noise_level=0.2):
    # Generate a time array
    t = np.linspace(0, 1, array_length)
    
    # Generate a noisy sine wave
    y = np.sin(2 * np.pi * t) + noise_level * np.random.normal(size=array_length)
    
    # Define the sine function to fit
    def sine_func(x, amplitude, frequency, phase):
        return amplitude * np.sin(2 * np.pi * frequency * x + phase)
    
    # Fit the sine function to the data
    popt, pcov = curve_fit(sine_func, t, y)
    
    # Generate the fitted curve
    y_fit = sine_func(t, *popt)
    
    # Plot the original noisy sine wave and the fitted curve
    fig, ax = plt.subplots()
    ax.plot(t, y, label='Noisy Sine Wave')
    ax.plot(t, y_fit, label='Fitted Curve', color='red')
    ax.legend()
    plt.show()
    
    return ax