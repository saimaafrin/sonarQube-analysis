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
        raise ValueError("df must be a pandas DataFrame")
    if "Status" not in df.columns:
        raise ValueError("df must contain the 'Status' column")
    status_counts = df["Status"].value_counts()
    status_counts = status_counts.sort_index()
    status_counts = status_counts.reset_index()
    status_counts = status_counts.rename(columns={"index": "Status", "Status": "Count"})
    fig, ax = plt.subplots()
    ax.pie(status_counts["Count"], labels=status_counts["Status"], autopct="%1.1f%%")
    ax.set_title("Status Distribution")
    return ax
df = pd.DataFrame({"Status": ["Pending", "In Progress", "Completed", "Cancelled", "Completed", "In Progress", "Pending", "Cancelled"]})