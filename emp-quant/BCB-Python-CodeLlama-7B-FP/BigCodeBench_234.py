import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
def task_func(df):
    """
    Perform a linear regression between "age" and "score" in the DataFrame, excluding rows with duplicate names.
    Plot the regression line and the scatter plot of the data.
    """
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")

    # Exclude rows with duplicate names
    df = df.drop_duplicates(subset=["name"])

    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(df["age"], df["score"])

    # Plot regression line
    plt.plot(df["age"], df["score"], "bo", label="Data")
    plt.plot(df["age"], slope * df["age"] + intercept, "r", label="Regression line")
    plt.legend()
    plt.xlabel("Age")
    plt.ylabel("Score")
    plt.title("Linear Regression")

    # Plot scatter plot
    plt.scatter(df["age"], df["score"], c="b")
    plt.xlabel("Age")
    plt.ylabel("Score")
    plt.title("Scatter Plot")

    # Return matplotlib.pyplot object and axes object
    return plt, plt.gca()
df = pd.DataFrame({"name": ["Alice", "Bob", "Charlie", "Alice", "Bob"],
                   "age": [25, 30, 35, 25, 30],
                   "score": [85, 90, 95, 80, 90]})