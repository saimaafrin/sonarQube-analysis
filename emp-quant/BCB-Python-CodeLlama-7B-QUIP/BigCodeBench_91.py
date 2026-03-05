
from scipy.stats import linregress
import matplotlib.pyplot as plt

def task_func(data, column1, column2):
    # Check if the specified columns exist in the DataFrame
    if column1 not in data.columns or column2 not in data.columns:
        raise ValueError("Columns do not exist in the DataFrame")

    # Perform linear regression on the specified columns
    result = linregress(data[column1], data[column2])

    # Create a plot of the original data and the fitted line
    fig, ax = plt.subplots()
    ax.plot(data[column1], data[column2])
    ax.plot(result.intercept + result.slope * data[column1], label="Fitted line")
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.set_title("Linear Regression")
    ax.legend()

    # Return the slope, intercept, r-value, p-value, and standard error of the regression
    return (result.slope, result.intercept, result.rvalue, result.pvalue, result.stderr)