
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def task_func(df, x_column, y_column):
    # Plot the scatter plot
    plt.scatter(df[x_column], df[y_column])

    # Fit the linear regression model
    model = LinearRegression().fit(df[x_column].values.reshape(-1, 1), df[y_column].values.reshape(-1, 1))

    # Overlay the predicted regression line on top in red
    plt.plot(df[x_column], model.predict(df[x_column].values.reshape(-1, 1)), color='red')

    # Return the Axes object containing the scatter plot and the linear regression line
    return plt.gca()