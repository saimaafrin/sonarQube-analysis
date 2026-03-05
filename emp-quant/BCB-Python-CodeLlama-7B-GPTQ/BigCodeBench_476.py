import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def task_func(X, Y):
    # Define the quadratic function
    def quadratic(X, a, b, c):
        return a * X ** 2 + b * X + c

    # Fit the data to the quadratic function
    popt, _ = curve_fit(quadratic, X, Y)

    # Plot the data and the fit
    plt.scatter(X, Y)
    plt.plot(X, quadratic(X, *popt), 'r-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Quadratic Fit')
    plt.show()

    # Return the optimized parameters and the plot
    return popt, plt.gca()
X = [1, 2, 3, 4, 5]
Y = [1, 4, 9, 16, 25]