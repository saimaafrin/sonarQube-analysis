from random import sample
import matplotlib.pyplot as plt
import pandas as pd
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df, tuples, n_plots):
    """
    Removes rows from a DataFrame based on values of multiple columns, and then creates n random line plots of two columns against each other.
    The function should output with:
        (pd.DataFrame, list): A tuple containing the modified DataFrame and a list of plot details.
        Each entry in the plot details list is a tuple containing the two columns plotted against each other.
    """
    # Remove rows from the DataFrame based on the values of the specified columns
    for col, val in tuples:
        df = df[df[col] != val]

    # Create n random line plots of two columns against each other
    plot_details = []
    for _ in range(n_plots):
        col1 = sample(COLUMNS, 1)[0]
        col2 = sample(COLUMNS, 1)[0]
        while col1 == col2:
            col2 = sample(COLUMNS, 1)[0]
        plot_details.append((col1, col2))

        # Create the plot
        fig, ax = plt.subplots()
        ax.plot(df[col1], df[col2])
        ax.set_xlabel(col1)
        ax.set_ylabel(col2)
        ax.set_title(f"{col1} vs {col2}")
        plt.show()

    return df, plot_details
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [1, 2, 3, 4, 5],
    'C': [1, 2, 3, 4, 5],
    'D': [1, 2, 3, 4, 5],
    'E': [1, 2, 3, 4, 5]
})
tuples = [('A', 3), ('B', 4)]
n_plots = 2