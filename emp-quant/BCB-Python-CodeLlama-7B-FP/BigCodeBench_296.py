import pandas as pd
import matplotlib.pyplot as plt
def task_func(df):
    """
    Draw a bar chart of the counts of each unique value in the 'value' column of a pandas DataFrame and return the Axes object.
    Empty DataFrame will return an empty bar chart.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df must be a pandas DataFrame.")

    # Get the unique values in the 'value' column
    unique_values = df["value"].unique()

    # Count the number of occurrences of each unique value
    value_counts = df["value"].value_counts()

    # Create a bar chart of the counts
    ax = value_counts.plot(kind="bar", title="Value Distribution", xlabel="Value", ylabel="Count")

    # Return the Axes object
    return ax
df = pd.DataFrame({"value": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})