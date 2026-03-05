import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def task_func(df, x_column, y_column):
    """
    Draws a scatter plot for the specified columns from a pandas DataFrame and fits a linear regression model to the data.
    Notes:
        - After plotting the scatterplot, this function overlays the predicted regression line on top in red on the same Axes.
        - The function should output with:
            - matplotlib.axes._axes.Axes: The Axes object containing the scatter plot and the linear regression line.
    """
    # Create a new figure and axis object
    fig, ax = plt.subplots()

    # Plot the scatter plot
    ax.scatter(df[x_column], df[y_column], c='blue')

    # Fit a linear regression model to the data
    model = LinearRegression()
    model.fit(df[x_column].values.reshape(-1, 1), df[y_column].values.reshape(-1, 1))

    # Overlay the predicted regression line on top in red
    ax.plot(df[x_column], model.predict(df[x_column].values.reshape(-1, 1)), c='red')

    # Return the Axes object containing the scatter plot and the linear regression line
    return ax
df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]})