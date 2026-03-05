from scipy.stats import linregress
import matplotlib.pyplot as plt
def task_func(data, column1, column2):
    """
    Perform a linear regression on two columns of a dataset and record the result.
    Additionally, generates a plot representing the original data and the fitted line.
    The function should raise the exception for: ValueError: If the specified columns do not exist in the DataFrame.
    The function should output with:
        tuple: The slope, intercept, r-value, p-value, and standard error of the regression.
        Axes: The matplotlib Axes object containing the plot.
    """
    # Check if the specified columns exist in the DataFrame
    if column1 not in data.columns or column2 not in data.columns:
        raise ValueError("The specified columns do not exist in the DataFrame.")

    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(data[column1], data[column2])

    # Generate plot
    fig, ax = plt.subplots()
    ax.plot(data[column1], data[column2], 'bo')
    ax.plot(data[column1], slope * data[column1] + intercept, 'r')
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.set_title("Linear Regression")
    return (slope, intercept, r_value, p_value, std_err), ax
data = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [2, 4, 6, 8, 10]})