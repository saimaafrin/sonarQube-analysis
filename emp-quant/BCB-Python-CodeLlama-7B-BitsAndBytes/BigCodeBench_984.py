
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def task_func(df, x_column, y_column):
    # Create a scatter plot of the data
    plt.scatter(df[x_column], df[y_column])

    # Fit a linear regression model to the data
    model = LinearRegression().fit(df[x_column], df[y_column])

    # Get the predicted values for the x-values
    x_pred = model.predict(df[x_column])

    # Overlay the predicted regression line on the scatter plot
    plt.plot(df[x_column], x_pred, color='red')

    # Return the Axes object containing the scatter plot and the linear regression line
    return plt.gca()