
import pandas as pd
import seaborn as sns

def task_func(df, col1, col2):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")

    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")

    # Check if the specified columns are in the DataFrame
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError("Columns not found in DataFrame")

    # Check if the data is numeric
    if not df[col1].dtype.kind in 'biufc':
        raise TypeError("Non-numeric data in column {}".format(col1))
    if not df[col2].dtype.kind in 'biufc':
        raise TypeError("Non-numeric data in column {}".format(col2))

    # Create a seaborn Axes object
    ax = sns.scatterplot(data=df, x=col1, y=col2)
    ax.set_title("Scatter Plot with Regression Line")
    ax.set_xlabel(col1)
    ax.set_ylabel(col2)

    # Add a regression line
    ax.plot(df[col1], df[col2], color='red')

    return ax