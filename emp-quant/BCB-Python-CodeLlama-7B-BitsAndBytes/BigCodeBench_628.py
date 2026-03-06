
import math
from random import randint
import matplotlib.pyplot as plt

def task_func():
    # Generate random frequency, amplitude, and phase shift
    frequency = randint(1, 10)
    amplitude = randint(1, 10)
    phase_shift = randint(0, 2 * math.pi)

    # Create and plot the sine wave
    x = np.linspace(0, 2 * math.pi, 1000)
    y = amplitude * np.sin(frequency * x + phase_shift)
    ax = plt.plot(x, y, label='Random Sine Wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Random Sine Wave')
    plt.show()

    return ax

# Call the function and plot the sine wave
ax = task_func()