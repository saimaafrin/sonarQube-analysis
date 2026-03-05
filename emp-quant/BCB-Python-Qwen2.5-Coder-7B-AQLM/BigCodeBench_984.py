
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def task_func(df, x_column, y_column):
    """
    Draws a scatter plot for the specified columns from a pandas DataFrame and fits a linear regression model to the data.
    After plotting the scatterplot, this function overlays the predicted regression line on top in red on the same Axes.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    x_column (str): The name of the column to be used as the x-axis.
    y_column (str): The name of the column to be used as the y-axis.
    
    Returns:
    matplotlib.axes._axes.Axes: The Axes object containing the scatter plot and the linear regression line.
    """
    # Extract the data for the specified columns
    x = df[x_column].values.reshape(-1, 1)
    y = df[y_column].values
    
    # Create a linear regression model
    model = LinearRegression()
    model.fit(x, y)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='blue', label='Data points')
    
    # Fit the regression line
    y_pred = model.predict(x)
    ax.plot(x, y_pred, color='red', label='Regression line')
    
    # Add labels and legend
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.legend()
    
    # Return the Axes object
    return ax