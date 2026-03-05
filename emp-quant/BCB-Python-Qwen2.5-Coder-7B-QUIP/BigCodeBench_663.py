
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def task_func(x, y, labels):
    def exp_func(x, a, b, c):
        return a * np.exp(-b * x) + c

    fig, axs = plt.subplots(len(labels), 1, figsize=(8, 6 * len(labels)))

    for ax, (xi, yi, label) in zip(axs, zip(x, y, labels)):
        popt, _ = curve_fit(exp_func, xi, yi)
        ax.plot(xi, yi, 'o', label='Data')
        ax.plot(xi, exp_func(xi, *popt), 'r-', label='Fitted Curve')
        ax.set_title(f'Fit for {label}')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()

    plt.tight_layout()
    plt.show()

    return fig