
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def task_func(l, x_data, plot=False):
    def func(x, a, b, c):
        return a * x ** 2 + b * x + c
    params, cov = curve_fit(func, x_data, l, p0=[1, 1, 1])
    fitted_values = func(x_data, *params)
    if plot:
        plt.plot(x_data, l, label='Original data')
        plt.plot(x_data, fitted_values, label='Fitted curve')
        plt.legend()
    return params, fitted_values, ax