
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def task_func(X, Y):
    return a * X**2 + b * X + c

# Load the data
X = [1, 2, 3, 4, 5]
Y = [1, 4, 9, 16, 25]

# Define the initial parameters
a = 1
b = 1
c = 1

# Define the function to optimize
def func(X, Y):
    return a * X**2 + b * X + c

# Define the parameters to optimize
parameters = [a, b, c]

# Define the bounds for the parameters
bounds = [(0, 10), (0, 10), (0, 10)]

# Perform the optimization
result = curve_fit(func, X, Y, parameters, bounds)

# Extract the optimized parameters
a, b, c = result.x

# Plot the data and the fit
plt.scatter(X, Y)
plt.plot(X, func(X, Y), 'r-')
plt.show()

# Print the optimized parameters
print(a, b, c)