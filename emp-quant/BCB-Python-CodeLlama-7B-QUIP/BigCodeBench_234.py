
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

def task_func(df):
    # Perform linear regression on the DataFrame
    model = stats.linregress(df['age'], df['score'])

    # Plot the regression line
    plt.plot(model.intercept + model.slope * df['age'])

    # Plot the scatter plot
    plt.scatter(df['age'], df['score'])

    # Set the labels and title
    plt.xlabel('Age')
    plt.ylabel('Score')
    plt.title('Linear Regression')

    # Return the matplotlib.pyplot object and the axes object
    return plt, plt.gca()