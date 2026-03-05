import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
def task_func(df):
    """
    Perform a linear regression between "age" and "score" in the DataFrame, excluding rows with duplicate names. Plot the regression line and the scatter plot of the data.
    Note that:
        - The function use "Linear Regression" for the plot title.
        - The function use "Age" and "Score" as the xlabel and ylabel respectively.
        - The function should raise the exception for: The function will raise a ValueError is input df is not a DataFrame.
        - The function should output with:
            - tuple: A tuple containing the matplotlib.pyplot object and the axes object.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame")

    # Perform linear regression
    X = df["age"]
    y = df["score"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()

    # Plot regression line and scatter plot
    fig, ax = plt.subplots()
    ax.plot(X, y, "bo", label="Scatter Plot")
    ax.plot(X, model.fittedvalues, "r", label="Regression Line")
    ax.set_xlabel("Age")
    ax.set_ylabel("Score")
    ax.set_title("Linear Regression")
    ax.legend()

    return fig, ax
df = pd.DataFrame({"age": [25, 30, 35, 40, 45], "score": [85, 90, 95, 100, 105]})