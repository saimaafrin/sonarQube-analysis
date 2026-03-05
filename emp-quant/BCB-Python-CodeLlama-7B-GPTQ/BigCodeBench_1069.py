import pandas as pd
import matplotlib.pyplot as plt
def task_func(data_dict):
    """
    Generates histograms for each column in the given DataFrame and checks if the value distributions are uniform.
    It prints a message for each non-uniform distribution.

    Args:
        data_dict (dict): A dictionary containing the data to be analyzed.

    Returns:
        List[plt.Axes]: A list of matplotlib Axes objects, each representing the histogram for a column.
    """
    # Create a Pandas DataFrame from the data dictionary
    df = pd.DataFrame(data_dict)

    # Create a list to store the matplotlib Axes objects
    ax_list = []

    # Iterate over the columns of the DataFrame
    for col in df.columns:
        # Generate a histogram for the current column
        ax = df[col].plot.hist(alpha=0.5, label=col)
        ax_list.append(ax)

        # Check if the distribution is uniform
        if not df[col].is_uniform:
            print(f"{col} is not uniform")

    # Return the list of matplotlib Axes objects
    return ax_list
data_dict = {
    "A": [1, 2, 3, 4, 5],
    "B": [1, 2, 3, 4, 5],
    "C": [1, 2, 3, 4, 5],
    "D": [1, 2, 3, 4, 5],
    "E": [1, 2, 3, 4, 5],
}