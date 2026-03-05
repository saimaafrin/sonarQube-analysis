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
    # Create a figure and an axes.
    fig, ax = plt.subplots()
    
    # Plot the scatter plot.
    ax.scatter(df[x_column], df[y_column], color='blue', label='Data points')
    
    # Fit a linear regression model.
    model = LinearRegression()
    model.fit(df[[x_column]], df[y_column])
    
    # Get the predicted values.
    y_pred = model.predict(df[[x_column]])
    
    # Plot the regression line.
    ax.plot(df[x_column], y_pred, color='red', label='Regression line')
    
    # Add labels and title.
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(f'Scatter plot and Linear Regression for {x_column} vs {y_column}')
    
    # Add a legend.
    ax.legend()
    
    # Show the plot.
    plt.show()
    
    # Return the axes object.
    return ax