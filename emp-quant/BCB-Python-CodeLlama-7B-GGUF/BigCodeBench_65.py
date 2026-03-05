
import pandas as pd
import matplotlib.pyplot as plt

COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=COLUMNS)

    # Group the DataFrame by the first n-1 columns
    grouped_df = df.groupby(COLUMNS[:-1])

    # Create a line chart with the last column as the y-axis
    ax = grouped_df.plot(kind='line', x=COLUMNS[:-1], y=COLUMNS[-1])

    # Set the x-label to the concatenation of all column names except the last one
    ax.set_xlabel('-'.join(COLUMNS[:-1]))

    # Set the y-label to the last column name
    ax.set_ylabel(COLUMNS[-1])

    return df, ax