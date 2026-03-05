import pandas as pd
import matplotlib.pyplot as plt
def task_func(df):
    """
    Draw a bar chart of the counts of each unique value in the 'value' column of a pandas DataFrame and return the Axes object.
    Empty DataFrame will return an empty bar chart.
    Note that:
        - This function use "Value Distribution" for the plot title.
        - This function use "Value" and "Count" as the xlabel and ylabel respectively.
    The function should raise the exception for:
        - The function will raise a ValueError is input df is not a DataFrame.
    The function should output with:
        - Axes: The matplotlib Axes object of the bar chart.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")

    # Create a new figure and axis object
    fig, ax = plt.subplots()

    # Create a bar chart of the counts of each unique value in the 'value' column
    ax.bar(df['value'].unique(), df['value'].value_counts())

    # Set the title of the plot
    ax.set_title("Value Distribution")

    # Set the xlabel of the plot
    ax.set_xlabel("Value")

    # Set the ylabel of the plot
    ax.set_ylabel("Count")

    # Return the Axes object
    return ax
df = pd.DataFrame({'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})