
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def task_func(X, Y):
    return a*X**2 + b*X + c

def main():
    # Generate some random data
    X = np.linspace(0, 10, 100)
    Y = np.sin(X) + np.random.normal(0, 0.1, size=100)

    # Fit the data to a quadratic function
    popt, _ = curve_fit(task_func, X, Y)

    # Plot the data and the fit
    fig, ax = plt.subplots()
    ax.scatter(X, Y)
    ax.plot(X, task_func(X, *popt))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Quadratic Fit')
    plt.show()

    # Print the optimized parameters
    print(popt)