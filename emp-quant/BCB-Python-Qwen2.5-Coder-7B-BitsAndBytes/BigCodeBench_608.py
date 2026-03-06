
import seaborn as sns
from random import sample

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df, tuples, n_plots):
    """
    Removes rows from a dataframe based on values of multiple columns,
    and then creates n random pairs of two columns against each other to generate pairplots.

    Parameters:
    df (pd.DataFrame): The input dataframe.
    tuples (list of tuples): List of tuples where each tuple contains column names to remove rows for.
    n_plots (int): Number of random pairs of columns to plot.

    Returns:
    tuple: A tuple containing:
        DataFrame: The modified DataFrame after removing specified rows.
        list of Axes: A list containing the generated pairplots.
    """
    # Remove rows based on specified column values
    for col1, col2 in tuples:
        df = df[(df[col1] != 0) & (df[col2] != 0)]

    # Create n random pairs of columns to plot
    columns_to_plot = sample(COLUMNS, min(2 * n_plots, len(COLUMNS)))
    pairplot_cols = [columns_to_plot[i:i+2] for i in range(0, len(columns_to_plot), 2)]
    
    # Generate pairplots
    pairplots = []
    for cols in pairplot_cols:
        pairplot = sns.pairplot(df[cols])
        pairplots.append(pairplot)

    return df, pairplots