
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def task_func(func, x_range=(-2, 2), num_points=1000):
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = func(x)
    integral = integrate.cumulative_trapezoidal(y, x)
    fig, ax = plt.subplots()
    ax.plot(x, y, label='Function')
    ax.plot(x, integral, label='Integral')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    return ax

ax = task_func(f)
ax.set_title('Plot of f(x) and its integral')
plt.show()