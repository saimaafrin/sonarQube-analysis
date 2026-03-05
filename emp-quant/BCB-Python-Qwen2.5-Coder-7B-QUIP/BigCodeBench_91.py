
from scipy.stats import linregress
import matplotlib.pyplot as plt

def task_func(data, column1, column2):
    """
    Perform a linear regression on two columns of a dataset and record the result.
    Additionally, generates a plot representing the original data and the fitted line.
    
    Parameters:
    data (pd.DataFrame): The DataFrame containing the dataset.
    column1 (str): The name of the first column for the regression.
    column2 (str): The name of the second column for the regression.
    
    Returns:
    tuple: The slope, intercept, r-value, p-value, and standard error of the regression.
    Axes: The matplotlib Axes object containing the plot.
    """
    # Check if the columns exist in the DataFrame
    if column1 not in data.columns or column2 not in data.columns:
        raise ValueError("The specified columns do not exist in the DataFrame.")
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(data[column1], data[column2])
    
    # Plot the original data and the fitted line
    fig, ax = plt.subplots()
    ax.scatter(data[column1], data[column2], label='Data')
    ax.plot(data[column1], data[column2], label='Fitted line', color='red')
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.legend()
    
    return (slope, intercept, r_value, p_value, std_err), ax