import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def task_func(df, x_column, y_column):
    # Create a scatter plot of the data
    plt.scatter(df[x_column], df[y_column])

    # Fit a linear regression model to the data
    model = LinearRegression()
    model.fit(df[x_column], df[y_column])

    # Overlay the predicted regression line on top of the scatter plot
    plt.plot(df[x_column], model.predict(df[x_column]), color='red')

    # Return the Axes object containing the scatter plot and the linear regression line
    return plt.gca()
df = pd.DataFrame({'x': np.random.rand(100), 'y': np.random.rand(100)})