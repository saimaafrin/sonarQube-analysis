import pandas as pd
import matplotlib.pyplot as plt
def task_func(df):
    """
    Draws a pie chart of the status distribution from a pandas DataFrame with a 'Status' column and returns the plot object.
    The 'Status' column in the DataFrame is expected to contain categorical data with possible values like 'Pending', 'In Progress', 'Completed', 'Cancelled'.
    The function should raise the exception for: ValueError: If 'df' is not a pandas DataFrame or does not contain the 'Status' column.
    The function should output with:
        matplotlib.axes.Axes: The Axes object with the pie chart.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' is not a pandas DataFrame")
    if "Status" not in df.columns:
        raise ValueError("'df' does not contain the 'Status' column")

    # Create a pie chart of the status distribution
    status_counts = df["Status"].value_counts()
    status_counts.plot(kind="pie", autopct="%1.1f%%", title="Status Distribution")

    # Return the plot object
    return plt.gca()
df = pd.DataFrame({"Status": ["Pending", "In Progress", "Completed", "Cancelled", "Pending", "In Progress", "Completed", "Cancelled"]})