import pandas as pd
import matplotlib.pyplot as plt
def task_func(data_dict):
    """
    Generates histograms for each column in the given DataFrame and checks if the value distributions are uniform.
    It prints a message for each non-uniform distribution.
    Returns a list of matplotlib Axes objects, each representing the histogram for a column.
    """
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data_dict)

    # Create a list to store the histogram Axes objects
    hist_axes = []

    # Iterate over each column in the DataFrame
    for col in df.columns:
        # Generate a histogram for the current column
        hist_ax = df[col].hist(bins=50, alpha=0.5, label=col)

        # Check if the distribution is uniform
        if not df[col].is_unique:
            print(f"{col} distribution is not uniform")

        # Add the histogram Axes object to the list
        hist_axes.append(hist_ax)

    # Return the list of histogram Axes objects
    return hist_axes
data_dict = {
    "A": [1, 2, 3, 4, 5],
    "B": [1, 2, 3, 4, 5],
    "C": [1, 2, 3, 4, 5],
    "D": [1, 2, 3, 4, 5],
    "E": [1, 2, 3, 4, 5],
}