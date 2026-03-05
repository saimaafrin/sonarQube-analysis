import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def task_func(df, x_column, y_column):
    """
    Draws a scatter plot for the specified columns from a pandas DataFrame and fits a linear regression model to the data.
    The function overlays the predicted regression line on top in red on the same Axes.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    x_column (str): The name of the column to be used as the x-axis.
    y_column (str): The name of the column to be used as the y-axis.

    Returns:
    matplotlib.axes._axes.Axes: The Axes object containing the scatter plot and the linear regression line.
    """
    # Extract the data for the specified columns
    x_data = df[x_column]
    y_data = df[y_column]

    # Create a scatter plot
    ax = plt.scatter(x_data, y_data, label='Data points')

    # Fit a linear regression model
    model = LinearRegression()
    model.fit(x_data.values.reshape(-1, 1), y_data)

    # Generate x values for the regression line
    x_line = x_data.min(), x_data.max()

    # Predict y values for the regression line
    y_line = model.predict(x_line.reshape(-1, 1))

    # Plot the regression line
    ax.plot(x_line, y_line, color='red', label='Regression line')

    # Add labels and legend
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.legend()

    # Show the plot
    plt.show()

    return ax