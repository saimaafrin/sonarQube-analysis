import pandas as pd
import matplotlib.pyplot as plt
def task_func(df, items=None, locations=None):
    """
    Generates a bar chart representing the distribution of specified items across given locations.
    The function takes a DataFrame with 'Item' and 'Location' columns and plots the count of each item per location.
    If lists of items and locations are provided, the chart will only include those specified, otherwise it defaults to a predefined list.
    The function should raise the exception for:
        ValueError: If 'df' is not a DataFrame, or if 'Item' or 'Location' columns are missing.
    The function should output with:
        matplotlib.axes.Axes: Axes object with the plotted bar chart.
    """
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a DataFrame")

    # Check if 'Item' and 'Location' columns are present
    if "Item" not in df.columns or "Location" not in df.columns:
        raise ValueError("'Item' and 'Location' columns must be present in the DataFrame")

    # Filter the DataFrame to include only the specified items and locations
    if items is not None and locations is not None:
        df = df[(df["Item"].isin(items)) & (df["Location"].isin(locations))]

    # Plot the bar chart
    ax = df.plot.bar(x="Location", y="Item", rot=0, figsize=(10, 6))

    # Set the title and x/y labels
    ax.set_title("Distribution of Items Across Locations")
    ax.set_xlabel("Location")
    ax.set_ylabel("Item")

    return ax
df = pd.DataFrame({
    "Item": ["A", "B", "C", "A", "B", "C"],
    "Location": ["X", "Y", "Z", "X", "Y", "Z"]
})