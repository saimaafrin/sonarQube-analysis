
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the quadratic function
def task_func(X, a, b, c):
    return a*X**2 + b*X + c

# Define the data
X = [1, 2, 3, 4, 5]
Y = [1, 4, 9, 16, 25]

# Fit the data to the quadratic function
popt, _ = curve_fit(task_func, X, Y)

# Plot the data and the fit
fig, ax = plt.subplots()
ax.scatter(X, Y)
ax.plot(X, task_func(X, *popt), color='red')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Quadratic Fit')

# Print the optimized parameters
print(popt)

# Show the plot
plt.show()