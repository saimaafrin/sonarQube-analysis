
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
    # Create a figure and an axes.
    fig, ax = plt.subplots()

    # Plot the scatter plot.
    ax.scatter(df[x_column], df[y_column], color='blue', label='Data points')

    # Fit a linear regression model.
    model = LinearRegression()
    model.fit(df[[x_column]], df[y_column])

    # Generate x values for the regression line.
    x_line = df[x_column].min(), df[x_column].max()

    # Predict y values for the regression line.
    y_line = model.predict(x_line.reshape(-1, 1))

    # Plot the regression line.
    ax.plot(x_line, y_line, color='red', label='Regression line')

    # Add labels and legend.
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.legend()

    # Show the plot.
    plt.show()

    # Return the Axes object.
    return ax