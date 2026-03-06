
from scipy.stats import linregress
import matplotlib.pyplot as plt

def task_func(data, column1, column2):
    """
    Perform a linear regression on two columns of a dataset and record the result.
    
    Parameters:
        data (pd.DataFrame): The input dataframe.
        column1 (str): The name of the first column.
        column2 (str): The name of the second column.
        
    Returns:
        tuple: The slope, intercept, r-value, p-value, and standard error of the regression.
        Axes: The matplotlib Axes object containing the plot.
    """
    # Check if the columns exist in the DataFrame
    if column1 not in data.columns or column2 not in data.columns:
        raise ValueError(f"One or both of the specified columns ({column1}, {column2}) do not exist in the DataFrame.")
    
    # Extract the data for the specified columns
    x = data[column1]
    y = data[column2]
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Data points')
    ax.plot(x, slope * x + intercept, color='red', label='Fitted line')
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.legend()
    
    return (slope, intercept, r_value, p_value, std_err), ax