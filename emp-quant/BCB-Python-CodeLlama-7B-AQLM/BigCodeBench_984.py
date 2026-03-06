import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def task_func(df, x_column, y_column):
    """
    Draws a scatter plot for the specified columns from a pandas DataFrame and fits a linear regression model to the data.

    Parameters:
    df (DataFrame): The input pandas DataFrame.
    x_column (str): The column name for the x-axis. Data contained in column must be numeric.
    y_column (str): The column name for the y-axis. Data contained in column must be numeric.

    Returns:
    matplotlib.axes._axes.Axes: The Axes object containing the scatter plot and the linear regression line.

    Requirements:
    - matplotlib
    - sklearn

    Notes:
    - After plotting the scatterplot, this function overlays the predicted regression line on top in red on the same Axes.

    Example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4]})
    >>> ax = task_func(df, 'A', 'B')
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    # Get the x and y data
    x = df[x_column].values
    y = df[y_column].values

    # Create a linear regression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(x.reshape(-1, 1), y)

    # Get the predicted y values
    y_pred = model.predict(x.reshape(-1, 1))

    # Plot the data
    plt.scatter(x, y, color='blue')
    plt.plot(x, y_pred, color='red')

    # Return the Axes object
    return plt.gca()