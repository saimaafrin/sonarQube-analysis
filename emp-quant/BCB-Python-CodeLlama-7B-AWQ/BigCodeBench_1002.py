import pandas as pd
import matplotlib.pyplot as plt
def task_func(data, column_name="target_column"):
    """
    Converts a given JSON data into a Pandas DataFrame and plots a histogram of a specified column.
    The function handles non-numeric columns by converting them to categorical type and then to numeric codes.
    It also checks if the specified column exists in the DataFrame.
    - The histogram's title is set to 'Histogram of <column_name>'.
    - The histogram's x-label are set to the name of the specified column.
    Exceptions:
    - ValueError: Raised if the specified column name does not exist in the DataFrame.
    """
    # Check if the specified column exists in the DataFrame
    if column_name not in data.columns:
        raise ValueError(f"Column {column_name} does not exist in the DataFrame")

    # Convert non-numeric columns to categorical type and then to numeric codes
    data = data.apply(pd.to_numeric, errors="coerce")

    # Create a Pandas DataFrame from the input JSON data
    df = pd.DataFrame(data)

    # Create a histogram plot of the specified column
    ax = df[column_name].plot.hist(title=f"Histogram of {column_name}", xlabel=column_name)

    # Return the DataFrame and the histogram plot
    return df, ax
data = {"a": [1, 2, 3, 4, 5], "b": ["a", "b", "c", "d", "e"]}