
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")

    # Perform linear regression
    X = df["age"]
    y = df["score"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()

    # Plot regression line and scatter plot
    fig, ax = plt.subplots()
    ax.scatter(X, y)
    ax.plot(X, model.fittedvalues, color="red")
    ax.set_xlabel("Age")
    ax.set_ylabel("Score")
    ax.set_title("Linear Regression")
    plt.show()

    return fig, ax