
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import get_window

def task_func(amplitude, frequency, time):
    # Generate the complex wave with Hann window
    window = get_window('hann', time, False)
    wave = amplitude * np.exp(1j * 2 * math.pi * frequency * time) * window
    return wave

# Plot the complex wave
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Complex Wave with Hann Window')
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.plot(wave.real, wave.imag)
ax.set_xlim(0, time[-1])
ax.set_ylim(-1, 1)
plt.show()

return wave, fig, ax