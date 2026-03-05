
import math
from random import randint
import matplotlib.pyplot as plt

def task_func():
    # Generate random frequency, amplitude, and phase shift
    frequency = randint(1, 10)
    amplitude = randint(1, 10)
    phase_shift = randint(0, 360)

    # Generate sine wave data
    x = np.linspace(0, 10, 1000)
    y = amplitude * np.sin(2 * math.pi * frequency * x + phase_shift)

    # Create and customize the plot
    fig, ax = plt.subplots()
    ax.set_title('Random Sine Wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.plot(x, y)

    return ax

# Call the function and display the plot
ax = task_func()
plt.show()