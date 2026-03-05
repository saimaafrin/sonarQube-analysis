
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(x):
    if not isinstance(x, np.ndarray):
        raise TypeError("x must be a numpy.ndarray")

    real_dist = norm(0, 1)
    imag_dist = norm(2, 2)

    complex_dist = real_dist + 1j * imag_dist

    return complex_dist

x = np.linspace(-5, 5, 100)
y = task_func(x)

plt.plot(x, y.real, label="Real part")
plt.plot(x, y.imag, label="Imaginary part")
plt.legend()
plt.show()