
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def task_func(df, x_column, y_column):
    """
    Draws a scatter plot for the specified columns from a pandas DataFrame and fits a linear regression model to the data.
    
    Parameters:
    df (pandas.DataFrame): The input DataFrame.
    x_column (str): The name of the column to be used as the independent variable.
    y_column (str): The name of the column to be used as the dependent variable.
    
    Returns:
    matplotlib.axes._axes.Axes: The Axes object containing the scatter plot and the linear regression line.
    """
    # Extract the data for plotting
    x = df[x_column]
    y = df[y_column]
    
    # Create a figure and an axes.
    fig, ax = plt.subplots()
    
    # Plot the scatter plot
    ax.scatter(x, y, color='blue', label='Data points')
    
    # Fit a linear regression model
    model = LinearRegression()
    model.fit(x.values.reshape(-1, 1), y)
    
    # Get the predicted values
    y_pred = model.predict(x.values.reshape(-1, 1))
    
    # Overlay the predicted regression line on top
    ax.plot(x, y_pred, color='red', label='Linear Regression Line')
    
    # Add labels and legend
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.legend()
    
    return ax