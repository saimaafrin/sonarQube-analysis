from scipy.stats import linregress
import matplotlib.pyplot as plt
def task_func(data, column1, column2):
    """
    Perform a linear regression on two columns of a dataset and record the result.
    Additionally, generates a plot representing the original data and the fitted line.
    
    Parameters:
    - data: pandas DataFrame containing the dataset.
    - column1: String, the name of the first column for regression.
    - column2: String, the name of the second column for regression.
    
    Returns:
    - tuple: The slope, intercept, r-value, p-value, and standard error of the regression.
    - Axes: The matplotlib Axes object containing the plot.
    """
    # Check if the specified columns exist in the DataFrame
    if column1 not in data.columns or column2 not in data.columns:
        raise ValueError(f"Columns {column1} and {column2} must exist in the DataFrame.")
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(data[column1], data[column2])
    
    # Plotting the original data and the fitted line
    fig, ax = plt.subplots()
    ax.scatter(data[column1], data[column2], color='blue', label='Data points')
    ax.plot(data[column1], slope * data[column1] + intercept, color='red', label='Fitted line')
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.legend()
    
    return (slope, intercept, r_value, p_value, std_err), ax