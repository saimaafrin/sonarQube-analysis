
from scipy.stats import linregress
import matplotlib.pyplot as plt

def task_func(data, column1, column2):
    # Check if the specified columns exist in the DataFrame
    if column1 not in data.columns or column2 not in data.columns:
        raise ValueError("The specified columns do not exist in the DataFrame")

    # Perform linear regression on the two columns
    slope, intercept, r_value, p_value, std_err = linregress(data[column1], data[column2])

    # Generate a plot of the original data and the fitted line
    fig, ax = plt.subplots()
    ax.scatter(data[column1], data[column2])
    ax.plot(data[column1], slope * data[column1] + intercept)
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.set_title("Linear Regression Plot")

    # Return the slope, intercept, r-value, p-value, and standard error of the regression
    return slope, intercept, r_value, p_value, std_err, ax

# Plot the results
ax.figure.show()