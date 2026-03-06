
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df must be a pandas DataFrame")

    # Get the unique values in the 'value' column
    unique_values = df['value'].unique()

    # Count the number of occurrences of each unique value
    value_counts = df['value'].value_counts()

    # Create a bar chart of the counts
    ax = value_counts.plot(kind='bar', title='Value Distribution', xlabel='Value', ylabel='Count')

    # Return the Axes object
    return ax