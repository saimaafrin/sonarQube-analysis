import pandas as pd
import matplotlib.pyplot as plt
def task_func(data):
    """
    Given a list of elements, each element is a list with the same length as COLUMNS, representing one row of a pandas DataFrame df to create.
    Draw a line chart with unique values in the COLUMNS[-1] of the pandas DataFrame "df", grouped by the rest of the columns.
    - The x-label should be set to the string obtained by joining all the column names (except the last one) by the character "-".
    - The y-label should be set to the last column name.
    The function should output with:
        tuple: A tuple containing:
        pandas.DataFrame: The DataFrame of the analyzed data.
        plt.Axes: The Axes object of the plotted line chart.
    """
    # Create a pandas DataFrame from the input data
    df = pd.DataFrame(data, columns=COLUMNS)

    # Group the DataFrame by the rest of the columns
    grouped_df = df.groupby(df.columns[:-1])

    # Create a line chart with the unique values in the last column
    ax = grouped_df.plot(kind='line', x=df.columns[:-1], y=df.columns[-1])

    # Set the x-label and y-label
    ax.set_xlabel('-'.join(df.columns[:-1]))
    ax.set_ylabel(df.columns[-1])

    # Return the DataFrame and Axes object
    return df, ax
data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]