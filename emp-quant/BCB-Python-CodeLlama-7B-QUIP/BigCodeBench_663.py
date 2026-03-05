
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def task_func(x, y, labels):
    # Define the function to fit
    def func(x, a, b, c):
        return a * np.exp(-b * x) + c

    # Initialize the parameters
    a = 1
    b = 1
    c = 0

    # Perform the curve_fit
    popt, _ = curve_fit(func, x, y, p0=np.array([a, b, c]))

    # Extract the parameters
    a = popt[0]
    b = popt[1]
    c = popt[2]

    # Plot the data and the fitted curve
    plt.plot(x, y, 'o', label=labels[0])
    plt.plot(x, func(x, a, b, c), 'k-', label=labels[1])

    # Set the labels and title
    plt.xlabel(labels[2])
    plt.ylabel(labels[3])
    plt.title(labels[4])

    # Return the figure
    return plt.gcf()

# Define the data
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
labels = ['Data', 'Fitted Curve', 'x', 'y', 'Title']

# Fit the curve and plot the data and the fitted curve
fig = task_func(x, y, labels)

# Show the figure
plt.show()