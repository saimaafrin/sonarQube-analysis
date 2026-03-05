import pandas as pd
import matplotlib.pyplot as plt
COLUMNS = ['col1', 'col2', 'col3']
def task_func(data):
    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data, columns=COLUMNS)

    # Group the DataFrame by the rest of the columns
    grouped_df = df.groupby(df.columns[:-1])

    # Create a line chart with unique values in the last column
    ax = grouped_df.plot(kind='line', x='-'.join(df.columns[:-1]), y=df.columns[-1])

    # Set the x-label to the string obtained by joining all the column names (except the last one) by the character "-"
    ax.set_xlabel('-'.join(df.columns[:-1]))

    # Set the y-label to the last column name
    ax.set_ylabel(df.columns[-1])

    # Return the DataFrame and the Axes object of the plotted line chart
    return df, ax
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
]