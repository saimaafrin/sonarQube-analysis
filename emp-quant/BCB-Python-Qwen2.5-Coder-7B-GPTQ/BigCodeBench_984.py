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

    # Create a figure and an axes object
    fig, ax = plt.subplots()

    # Plot the scatter plot
    ax.scatter(x_data, y_data, color='blue', label='Data points')

    # Fit a linear regression model
    model = LinearRegression()
    model.fit(x_data.values.reshape(-1, 1), y_data.values.reshape(-1, 1))

    # Get the predicted values
    y_pred = model.predict(x_data.values.reshape(-1, 1))

    # Plot the regression line
    ax.plot(x_data, y_pred, color='red', label='Regression line')

    # Add labels and legend
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.legend()

    # Return the axes object
    return ax