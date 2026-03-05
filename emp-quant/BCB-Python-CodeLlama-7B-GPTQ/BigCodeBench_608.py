import seaborn as sns
from random import sample
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df, tuples, n_plots):
    """
    Remove rows from a dataframe based on values of multiple columns, and then create n random pairs of two columns against each other to generate pairplots.
    The function should output with:
        tuple: A tuple containing:
            DataFrame: The modified DataFrame after removing specified rows.
            list of Axes: A list containing the generated pairplots.
    """
    # Remove rows from the dataframe based on the specified tuples
    for col, val in tuples:
        df = df[df[col] != val]

    # Create n random pairs of two columns against each other
    pairs = sample(COLUMNS, n_plots)

    # Generate pairplots
    ax_list = []
    for pair in pairs:
        ax = sns.pairplot(df, x_vars=pair[0], y_vars=pair[1])
        ax_list.append(ax)

    return df, ax_list
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [1, 2, 3, 4, 5],
    'C': [1, 2, 3, 4, 5],
    'D': [1, 2, 3, 4, 5],
    'E': [1, 2, 3, 4, 5]
})
tuples = [('A', 3)]
n_plots = 2