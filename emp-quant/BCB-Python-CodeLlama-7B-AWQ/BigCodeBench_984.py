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
    ax.scatter(df[x_column], df[y_column])

    # Fit a linear regression model to the data
    model = LinearRegression()
    model.fit(df[x_column], df[y_column])

    # Plot the predicted regression line
    ax.plot(df[x_column], model.predict(df[x_column]), color='red')

    # Return the Axes object
    return ax
df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]})