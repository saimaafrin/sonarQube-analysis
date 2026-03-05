
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def task_func(df, x_column, y_column):
    # Plot the scatter plot
    ax = plt.scatter(df[x_column], df[y_column])

    # Fit the linear regression model
    model = LinearRegression().fit(df[x_column], df[y_column])

    # Overlay the regression line on the scatter plot
    ax.plot(model.predict(df[x_column]), color='red')

    return ax