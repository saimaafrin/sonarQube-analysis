
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def task_func(df, x_column, y_column):
    # Extract the data for the specified columns
    x = df[x_column].values.reshape(-1, 1)
    y = df[y_column].values

    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='blue', label='Data')

    # Fit a linear regression model
    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)

    # Plot the regression line
    ax.plot(x, y_pred, color='red', label='Regression Line')

    # Add labels and title
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(f'Scatter Plot and Regression Line for {x_column} vs {y_column}')
    ax.legend()

    # Return the Axes object
    return ax